from django.db.models import Max

from oscar.apps.catalogue.abstract_models import AbstractProduct

class Product(AbstractProduct):

    def is_popular(self):
        if self.stats.score:
            same_class_products = self.get_product_class().products
            max_score = same_class_products.aggregate(Max('stats__score'))['stats__score__max']
            if self.stats.score / max_score >= 0.8:
                return True
        return False

from oscar.apps.catalogue.models import *