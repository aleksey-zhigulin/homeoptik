from oscar.core.loading import get_class


CoreCheckoutSessionData = get_class('checkout.utils', 'CheckoutSessionData')


class CheckoutSessionData(CoreCheckoutSessionData):

    def ship_to_pickup_address(self, address):
        """
        Use an user address (from an address book) as the shipping address.
        """
        self._set('shipping', 'pickup_address_id', address.id)

    def use_shipping_method(self, code):
        """
        Set shipping method code to session
        """
        self.reset_shipping_data()
        self._set('shipping', 'method_code', code)

    def ship_to_user_address(self, address):
        """
        Use an user address (from an address book) as the shipping address.
        """
        self._set('shipping', 'user_address_id', address.id)

    def shipping_pickup_address_id(self):
        """
        Return user address id
        """
        return self._get('shipping', 'pickup_address_id')

    def is_shipping_address_set(self):
        """
        Test whether a shipping address has been stored in the session.

        This can be from a new address or re-using an existing address.
        """
        new_fields = self.new_shipping_address_fields()
        has_new_address = new_fields is not None
        user_address_id = self.shipping_user_address_id()
        has_old_address = user_address_id is not None and user_address_id > 0
        pickup_address_id = self.shipping_pickup_address_id()
        has_pickup_address = pickup_address_id is not None and pickup_address_id > 0
        return has_new_address or has_old_address or has_pickup_address