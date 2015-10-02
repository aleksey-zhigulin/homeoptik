__author__ = 'aleksey'

from oscar.core.loading import get_model
from oscar.apps.checkout.forms import ShippingAddressForm as OldShippingAddressForm

class ShippingAddressForm(OldShippingAddressForm):

    class Meta:
        model = get_model('order', 'shippingaddress')

        fields = [
            'first_name', 'line1', 'country', 'phone_number', 'notes',
        ]
