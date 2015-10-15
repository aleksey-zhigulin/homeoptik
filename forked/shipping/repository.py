from decimal import Decimal as D

from django.core.exceptions import ImproperlyConfigured
from django.utils.translation import ugettext_lazy as _

from oscar.apps.shipping import repository

from forked.shipping import methods as shipping_methods

class Repository(repository.Repository):

    methods = (shipping_methods.Free(), shipping_methods.Pickup())