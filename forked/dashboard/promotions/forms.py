from django.utils.translation import ugettext_lazy as _

from oscar.apps.dashboard.promotions.forms import *
from oscar.apps.dashboard.promotions.forms import PagePromotionForm as CorePagePromotionForm

from forked.promotions.conf import PROMOTION_CLASSES

Slide = get_class('promotions.models', 'Slide')

class PagePromotionForm(CorePagePromotionForm):

    class Meta:
        model = PagePromotion
        fields = ['position', 'page_url']


class PromotionTypeSelectForm(forms.Form):
    choices = []
    for klass in PROMOTION_CLASSES:
        choices.append((klass.classname(), klass._meta.verbose_name))
        promotion_type = forms.ChoiceField(choices=tuple(choices),
                                           label=_("Promotion type"))


class SlideForm(forms.ModelForm):
    class Meta:
        model = Slide
        fields = ['name', 'link_url', 'image', 'body']

    def __init__(self, *args, **kwargs):
        super(SlideForm, self).__init__(*args, **kwargs)
        self.fields['body'].widget.attrs['class'] = "no-widget-init"
