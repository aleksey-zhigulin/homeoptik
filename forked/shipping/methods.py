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



