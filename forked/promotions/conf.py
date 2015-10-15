from models import Slide
from oscar.apps.promotions.conf import *

def get_promotion_classes():
    return (RawHTML, Image, Slide, SingleProduct,
            AutomaticProductList, HandPickedProductList, MultiImage)

PROMOTION_CLASSES = get_promotion_classes()
