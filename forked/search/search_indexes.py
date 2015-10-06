# -*- coding: utf-8 -*-

from haystack import indexes

from oscar.apps.search.search_indexes import ProductIndex as CoreProductIndex
from oscar.apps.catalogue.models import ProductAttributeValue

class ProductIndex(CoreProductIndex):

    glass_style = indexes.CharField(null=True, faceted=True)

    def prepare_glass_style(self, obj):
        try:
            print obj.attribute_values.get(attribute__name='Форма').value_as_text
        except ProductAttributeValue.DoesNotExist:
            return None
        return obj.attribute_values.get(attribute__name='Форма').value_as_text
