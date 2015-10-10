from oscar.apps.dashboard.promotions.views import *
from oscar.core.loading import get_class

from forked.promotions.conf import PROMOTION_CLASSES
from forked.promotions.models import Slide


from forms import PromotionTypeSelectForm as SelectForm

SlideForm = get_class('dashboard.promotions.forms', 'SlideForm')

class ListView(generic.TemplateView):
    template_name = 'dashboard/promotions/promotion_list.html'

    def get_context_data(self):
        # Need to load all promotions of all types and chain them together
        # no pagination required for now.
        data = []
        num_promotions = 0
        for klass in PROMOTION_CLASSES:
            objects = klass.objects.all()
            num_promotions += objects.count()
            data.append(objects)
        promotions = itertools.chain(*data)
        ctx = {
            'num_promotions': num_promotions,
            'promotions': promotions,
            'select_form': SelectForm(),
            }
        return ctx

class CreateRedirectView(generic.RedirectView):
    permanent = True

    def get_redirect_url(self, **kwargs):
        code = self.request.GET.get('promotion_type', None)
        urls = {}
        print PROMOTION_CLASSES
        for klass in PROMOTION_CLASSES:
            urls[klass.classname()] = reverse('dashboard:promotion-create-%s' %
                                              klass.classname())
        return urls.get(code, None)

class CreateSlideView(CreateView):
    model = Slide
    form_class = SlideForm

class UpdateSlideView(UpdateView):
    model = Slide
    form_class = SlideForm

class DeleteSlideView(DeleteView):
    model = Slide