__author__ = 'aleksey'

from django import template

register = template.Library()

@register.assignment_tag
def nearest_pages(current, total):

    """{% nearest_pages current total %} return maximum 5 pages near current page number"""

    first = max(1, min(total - 4, current - 2))
    last = min(total + 1, first + 5)
    return range(first, last)