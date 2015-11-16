# -*- coding: utf-8 -*-
from django import forms
from django.conf import settings

from yandex_money.models import Payment
from yandex_money.forms import BasePaymentForm

from oscar.core.loading import get_model
from oscar.apps.checkout.forms import ShippingAddressForm as OldShippingAddressForm

class ShippingAddressForm(OldShippingAddressForm):

    class Meta:
        model = get_model('order', 'shippingaddress')

        fields = [
            'first_name', 'line1', 'country', 'phone_number', 'notes',
            ]





class PaymentMethodsForm(forms.Form):

    paymentType = forms.CharField(label=u'Способ оплаты',
                                  widget=forms.Select(choices=settings.PAYMENT_METHODS + Payment.PAYMENT_TYPE.CHOICES),
                                  min_length=2, max_length=2,
                                  initial=Payment.PAYMENT_TYPE.PC)

    def __init__(self, *args, **kwargs):
        super(PaymentMethodsForm, self).__init__(*args, **kwargs)
        if hasattr(settings, 'YANDEX_ALLOWED_PAYMENT_TYPES'):
            allowed_payment_types = settings.YANDEX_ALLOWED_PAYMENT_TYPES
            self.fields['paymentType'].widget.choices = filter(
                lambda x: x[0] in allowed_payment_types,
                self.fields['paymentType'].widget.choices) + settings.PAYMENT_METHODS


