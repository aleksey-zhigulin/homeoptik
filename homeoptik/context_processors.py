__author__ = 'aleksey'


from newsletter_subscription.backend import ModelBackend
from newsletter_subscription.views import NewsletterForm

from models import Subscription

def subscribe_form(request):
    form = NewsletterForm(
        request.POST or None,
        backend=ModelBackend(Subscription),
        request=request,
        initial={
            'email': request.user.email,
            'action': 'subscribe',
        } if request.user.is_authenticated() else {
            'action': 'subscribe',
        },
    )
    return {
        'subscribe_form': form,
        }