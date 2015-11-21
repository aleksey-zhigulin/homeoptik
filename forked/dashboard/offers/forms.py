from oscar.apps.dashboard.offers.forms import *

from forked.offer import models

class MetaDataForm(forms.ModelForm):
    class Meta:
        model = models.ConditionalOffer
        fields = ('name', 'description', 'image')
