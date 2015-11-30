# -*- coding: utf-8 -*-

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from oscar.apps.shipping.methods import *


class Pickup(FixedPrice):

    code = 'pickup-shipping'
    name = _('Pickup')
    description = _('Customer pickup order by himself')
    charge_excl_tax = settings.OSCAR_SHIPPING_PICKUP_EXCL_TAX
    charge_incl_tax = settings.OSCAR_SHIPPING_PICKUP_INCL_TAX

class Courier(FixedPrice):

    code = 'courier-shipping'
    name = _('Courier')
    description = _('Shipping by courier in Moscow')
    charge_excl_tax = settings.OSCAR_SHIPPING_COURIER_EXCL_TAX
    charge_incl_tax = settings.OSCAR_SHIPPING_COURIER_INCL_TAX

class Post(FixedPrice):

    code = 'post-shipping'
    name = _('Post')
    description = _('Shipping by Russian Post')
    charge_excl_tax = settings.OSCAR_SHIPPING_POST_EXCL_TAX
    charge_incl_tax = settings.OSCAR_SHIPPING_POST_INCL_TAX


