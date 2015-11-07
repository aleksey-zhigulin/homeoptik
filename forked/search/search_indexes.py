# -*- coding: utf-8 -*-

from haystack import indexes

from oscar.apps.search.search_indexes import ProductIndex as CoreProductIndex
from oscar.apps.catalogue.models import ProductAttributeValue

class ProductIndex(CoreProductIndex):

    # Линзы для очков
    # astigmatic = indexes.CharField(null=True, faceted=True)
    # color = indexes.CharField(null=True, faceted=True)
    # design = indexes.CharField(null=True, faceted=True)
    # manufacturer = indexes.CharField(null=True, faceted=True)
    # warranty = indexes.CharField(null=True, faceted=True)
    brand = indexes.CharField(null=True, faceted=True)
    cover = indexes.CharField(null=True, faceted=True)
    index = indexes.DecimalField(null=True, faceted=True)
    lenses_type = indexes.CharField(null=True, faceted=True)
    material = indexes.CharField(null=True, faceted=True)
    properties = indexes.CharField(null=True, faceted=True)
    purpose = indexes.CharField(null=True, faceted=True)
    reflex = indexes.CharField(null=True, faceted=True)

    # def prepare_astigmatic(self, obj):
    #     try:
    #         return obj.attribute_values.get(attribute__code='Astigmatic').value_as_text
    #     except ProductAttributeValue.DoesNotExist:
    #         return None

    def prepare_brand(self, obj):
        try:
            return obj.attribute_values.get(attribute__code='Brand').value_as_text
        except ProductAttributeValue.DoesNotExist:
            return None

    # def prepare_color(self, obj):
    #     try:
    #         return obj.attribute_values.get(attribute__code='Color').value_as_text
    #     except ProductAttributeValue.DoesNotExist:
    #         return None

    def prepare_cover(self, obj):
        try:
            return obj.attribute_values.get(attribute__code='Cover').value_as_text
        except ProductAttributeValue.DoesNotExist:
            return None

    # def prepare_design(self, obj):
    #     try:
    #         return obj.attribute_values.get(attribute__code='Design').value_as_text
    #     except ProductAttributeValue.DoesNotExist:
    #         return None

    def prepare_index(self, obj):
        try:
            return obj.attribute_values.get(attribute__code='Index').value
        except ProductAttributeValue.DoesNotExist:
            return None

    def prepare_lenses_type(self, obj):
        try:
            return obj.attribute_values.get(attribute__code='Lenses_type').value_as_text
        except ProductAttributeValue.DoesNotExist:
            return None

    def prepare_manufacturer(self, obj):
        try:
            return obj.attribute_values.get(attribute__code='Manufacturer').value_as_text
        except ProductAttributeValue.DoesNotExist:
            return None

    def prepare_material(self, obj):
        try:
            return obj.attribute_values.get(attribute__code='Material').value_as_text
        except ProductAttributeValue.DoesNotExist:
            return None

    def prepare_properties(self, obj):
        try:
            return obj.attribute_values.get(attribute__code='Properties').value_as_text
        except ProductAttributeValue.DoesNotExist:
            return None

    def prepare_purpose(self, obj):
        try:
            return obj.attribute_values.get(attribute__code='Purpose').value_as_text
        except ProductAttributeValue.DoesNotExist:
            return None

    def prepare_reflex(self, obj):
        try:
            return obj.attribute_values.get(attribute__code='Reflex').value_as_text
        except ProductAttributeValue.DoesNotExist:
            return None

    # def prepare_warranty(self, obj):
    #     try:
    #         return obj.attribute_values.get(attribute__code='Warranty').value_as_text
    #     except ProductAttributeValue.DoesNotExist:
    #         return None