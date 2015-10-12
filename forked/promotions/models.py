from django.db import models
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _, pgettext_lazy
from django.core.urlresolvers import reverse
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from oscar.core.loading import get_model

from oscar.models.fields import ExtendedURLField

from oscar.apps.promotions.models import AbstractPromotion

@python_2_unicode_compatible
class Slide(AbstractPromotion):
    """
    Slide for bxslider
    """
    _type = 'Slide'
    name = models.CharField(_("Name"), max_length=128)
    image = models.ImageField(
        _('Image'), upload_to=settings.OSCAR_PROMOTION_FOLDER,
        max_length=255)
    link_url = ExtendedURLField(
        _('Link URL'), blank=True,
        help_text=_('This is where this promotion links to'))
    body = models.TextField(_("BxSlider text block in HTML"))
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'promotions'
        verbose_name = _("Slide")
        verbose_name_plural = _("Slide")

from oscar.apps.promotions.models import *  # noqa

