from django import http
from django.contrib import messages
from django.http import HttpResponseRedirect, QueryDict
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import redirect
from django.views import generic
from django.utils.translation import ugettext as _

from oscar.apps.checkout import views
from oscar.apps.payment import forms, models
from oscar.apps.shipping.methods import NoShippingRequired
from oscar.core.loading import get_class, get_classes, get_model

from yandex_money.models import Payment
from yandex_money.forms import PaymentForm

from .forms import PaymentMethodsForm
from .facade import yandexkassa_redirect
from forked.address.models import PickupAddress

# PickupAddress = get_model('address', 'PickupAddress')
CheckoutSessionMixin = get_class('checkout.session', 'CheckoutSessionMixin')
CoreIndexView = get_class('checkout.views', 'IndexView')
CoreShippingAddressView = get_class('checkout.views', 'ShippingAddressView')
CoreShippingMethodView = get_class('checkout.views', 'ShippingMethodView')
RedirectRequired, UnableToTakePayment, PaymentError \
    = get_classes('payment.exceptions', ['RedirectRequired',
                                         'UnableToTakePayment',
                                         'PaymentError'])
Repository = get_class('shipping.repository', 'Repository')
UserAddress = get_model('address', 'UserAddress')


class IndexView(CoreIndexView):

    success_url = reverse_lazy('checkout:shipping-method')


class ShippingAddressPickupView(CheckoutSessionMixin, generic.TemplateView):
    """
    Determine the shipping address for the order.

    The default behaviour is to display a list of addresses from the users's
    address book, from which the user can choose one to be their shipping
    address.  They can add/edit/delete these USER addresses.  This address will
    be automatically converted into a SHIPPING address when the user checks
    out.

    Alternatively, the user can enter a SHIPPING address directly which will be
    saved in the session and later saved as ShippingAddress model when the
    order is successfully submitted.
    """
    template_name = 'checkout/shipping_address_pickup.html'
    success_url = reverse_lazy('checkout:payment-method')
    pre_conditions = ['check_basket_is_not_empty',
                      'check_basket_is_valid',
                      'check_user_email_is_captured']
    skip_conditions = ['skip_unless_basket_requires_shipping']

    def get_context_data(self, **kwargs):
        ctx = super(ShippingAddressPickupView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated():
            # Look up address book data
            ctx['addresses'] = self.get_available_addresses()
        return ctx

    def get_available_addresses(self):
        return PickupAddress.objects.all()

    def post(self, request, *args, **kwargs):
        # Check if a shipping address was selected directly (eg no form was
        address = PickupAddress.objects.get(
            pk=self.request.POST['address_id'])
        print("post", address)
        action = self.request.POST.get('action', None)
        if action == 'ship_to':
            # User has selected a previous address to ship to
            self.checkout_session.ship_to_pickup_address(address)
            return redirect(self.success_url)
        else:
            return http.HttpResponseBadRequest()


class ShippingAddressView(CoreShippingAddressView):

    success_url = reverse_lazy('checkout:payment-method')
    pre_conditions = ['check_basket_is_not_empty',
                      'check_basket_is_valid',
                      'check_user_email_is_captured',]

    def get(self, request, *args, **kwargs):
        if not self.checkout_session.is_shipping_method_set(self.request.basket):
            return redirect('checkout:shipping-method')
        elif self.checkout_session.shipping_method_code(self.request.basket) == 'pickup-shipping':
            return redirect('checkout:shipping-address-pickup')
        return super(ShippingAddressView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # Check if a shipping address was selected directly (eg no form was
        # filled in)
        if self.request.user.is_authenticated() \
                and 'address_id' in self.request.POST:
            address = UserAddress._default_manager.get(
                pk=self.request.POST['address_id'], user=self.request.user)
            action = self.request.POST.get('action', None)
            if action == 'ship_to':
                # User has selected a previous address to ship to
                self.checkout_session.ship_to_user_address(address)
                print(self.get_success_url())
                return redirect(self.get_success_url())
            else:
                return http.HttpResponseBadRequest()
        else:
            return super(ShippingAddressView, self).post(
                request, *args, **kwargs)

class ShippingMethodView(CoreShippingMethodView):

    template_name = 'checkout/shipping_methods.html'
    pre_conditions = ['check_basket_is_not_empty',
                      'check_basket_is_valid',
                      'check_user_email_is_captured']

    def get(self, request, *args, **kwargs):

        self._methods = self.get_available_shipping_methods()
        if len(self._methods) == 1:
            # Only one shipping method - set this and redirect onto the next
            # step
            self.checkout_session.use_shipping_method(self._methods[0].code)
            return self.get_success_response()

        # Must be more than one available shipping method, we present them to
        # the user to make a choice.
        return super(ShippingMethodView, self).get(request, *args, **kwargs)

    def get_available_shipping_methods(self):
        """
        Returns all applicable shipping method objects for a given basket.
        """
        return Repository().get_shipping_methods(
            basket=self.request.basket, user=self.request.user,
            shipping_addr=None,
            request=self.request)

    def get_success_response(self):
        if self.checkout_session.shipping_method_code(self.request.basket) == 'pickup-shipping':
            return redirect('checkout:shipping-address-pickup')
        else:
            return redirect('checkout:shipping-address')


class PaymentMethodView(CheckoutSessionMixin, generic.TemplateView):

    template_name = 'checkout/payment_methods.html'
    pre_conditions = [
        'check_basket_is_not_empty',
        'check_basket_is_valid',
        'check_user_email_is_captured',
        'check_shipping_data_is_captured']
    skip_conditions = ['skip_unless_payment_is_required']

    def get_context_data(self, **kwargs):
        ctx = super(PaymentMethodView, self).get_context_data(**kwargs)

        payment_method = self.checkout_session.payment_method()
        if payment_method:
            ctx['payment_method_form'] = PaymentMethodsForm({'paymentType': payment_method})
        else:
            ctx['payment_method_form'] = PaymentMethodsForm()
        return ctx

    def post(self, request, *args, **kwargs):
        payment_type = request.POST.get('paymentType', None)
        if not payment_type:
            messages.error(request, _("Your submitted payment method is not"
                                      " permitted"))
            return redirect('checkout:payment-method')

        # Save the code for the chosen payment method in the session
        # and continue to the next step.
        self.checkout_session.pay_by(payment_type)

        return self.get_success_response()

    def get_success_response(self):
        return redirect('checkout:preview')


# class PaymentDetailsView(views.PaymentDetailsView):
#
#     def handle_payment(self, order_number, total, **kwargs):
#         payment = Payment(
#             order_amount=total.incl_tax,
#             order_number=order_number,
#             payment_type=self.checkout_session.payment_method()
#             # cps_phone=,
#             # cps_email
#         )
#         payment.save()
#         return yandexkassa_redirect(self.request, payment.id)
#

class PaymentYandexView(generic.TemplateView):

    template_name = 'checkout/payment_yandex.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        payment = Payment.objects.get(id=int(context['payment_id']))
        context['payment_form'] = PaymentForm(instance=payment)
        return self.render_to_response(context)



