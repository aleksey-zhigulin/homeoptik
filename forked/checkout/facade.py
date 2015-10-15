# set encoding=utf-8

# from logging import getLogger
# log = getLogger('yandexkassa.facade')

from django.core.urlresolvers import reverse
from oscar.core.loading import get_class

from yandex_money.models import Payment
from yandex_money.forms import PaymentForm


# from robokassa.forms import RobokassaForm
# from robokassa.conf import EXTRA_PARAMS

RedirectRequired = get_class('payment.exceptions','RedirectRequired')

def yandexkassa_redirect(request, payment_id, **kwargs):

    # session = request.session
    # session.save()
    # if session.session_key is not None:
    #     initial['session_key'] = session.session_key
    # else:
    #     log.error('session_key is empty'


    err = RedirectRequired(reverse('checkout:payment-yandex', kwargs={'payment_id': payment_id}))
    raise err




