from oscar.apps.promotions.views import HomeView as CoreHomeView
from oscar.apps.customer.history import get as get_recently_viewed

from oscar.core.loading import get_model

Product = get_model('catalogue', 'product')

class HomeView(CoreHomeView):

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['popular_products'] = Product.objects.filter(stats__isnull=False).order_by('-stats__score')[:4]
        context['newest_products'] = Product.objects.order_by('-date_created')[:4]
        context['latest_products'] = get_recently_viewed(self.request)[:4]
        return context