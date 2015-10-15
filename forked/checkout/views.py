from django.contrib import messages
from django.http import HttpResponseRedirect, QueryDict
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.views import generic
from django.utils.translation import ugettext as _

from oscar.apps.checkout import views
from oscar.apps.payment import forms, models
from oscar.core.loading import get_class, get_classes

from yandex_money.models import Payment
from yandex_money.forms import PaymentForm

from .forms import PaymentMethodsForm
from .facade import yandexkassa_redirect

CheckoutSessionMixin = get_class('checkout.session', 'CheckoutSessionMixin')
RedirectRequired, UnableToTakePayment, PaymentError \
    = get_classes('payment.exceptions', ['RedirectRequired',
                                         'UnableToTakePayment',
                                         'PaymentError'])

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

        ctx['payment_method_form'] = PaymentMethodsForm(
            {'paymentType': self.checkout_session.payment_method()}
        )
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


class PaymentDetailsView(views.PaymentDetailsView):

    def handle_payment(self, order_number, total, **kwargs):
        payment = Payment(
            order_amount=total.incl_tax,
            order_number=order_number,
            payment_type=self.checkout_session.payment_method()
            # cps_phone=,
            # cps_email
        )
        payment.save()
        return yandexkassa_redirect(self.request, payment.id)


class PaymentYandexView(generic.TemplateView):

    template_name = 'checkout/payment_yandex.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        payment = Payment.objects.get(id=int(context['payment_id']))
        context['payment_form'] = PaymentForm(instance=payment)
        return self.render_to_response(context)



