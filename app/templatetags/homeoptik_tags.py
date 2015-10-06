__author__ = 'aleksey'

from django import template

from oscar.core.loading import get_model

ConditionalOffer = get_model('offer', 'ConditionalOffer')

register = template.Library()

@register.assignment_tag
def nearest_pages(current, total):

    """{% nearest_pages current total %} return maximum 5 pages near current page number"""

    first = max(1, min(total - 4, current - 2))
    last = min(total + 1, first + 5)
    return range(first, last)

@register.assignment_tag
def get_offers_list():

    """return offers list"""

    return ConditionalOffer.active.filter(offer_type=ConditionalOffer.SITE)


@register.assignment_tag(takes_context=True)
def has_choice(context):
    return sum(i['count'] for i in context['items']) > 0 and \
        sum(i['disabled'] for i in context['items']) + 1 < len(context['items'])