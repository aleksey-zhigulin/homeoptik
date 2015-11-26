from oscar.apps.promotions.views import HomeView as CoreHomeView
from oscar.apps.customer.history import get as get_recently_viewed

from oscar.core.loading import get_model

Product = get_model('catalogue', 'product')
ConditionalOffer = get_model('offer', 'ConditionalOffer')

class HomeView(CoreHomeView):

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['popular_products'] = Product.objects.filter(stats__isnull=False).order_by('-stats__score')[:8]
        context['newest_products'] = Product.objects.order_by('-date_created')[:8]

        offers = ConditionalOffer.active.filter(offer_type=ConditionalOffer.SITE)
        products = []
        for offer in offers:
            cnt = len(products)
            if cnt == 8: break
            products.extend(offer.products()[:8 - cnt])
        context['sale_products'] = products
        return context