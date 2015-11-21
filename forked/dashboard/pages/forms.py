from oscar.apps.dashboard.pages.forms import *
from oscar.apps.dashboard.pages.forms import PageUpdateForm as CorePageUpdateForm

class PageUpdateForm(CorePageUpdateForm):

    class Meta:
        model = FlatPage
        fields = ('title', 'subheader', 'url', 'content', 'image')

