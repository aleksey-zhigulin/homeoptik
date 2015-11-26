# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from oscar.core.loading import get_class, get_model

from forked.flatpages.models import FlatPage
from forms import ContactForm

from settings import CONTACT_FORM_BCC

Dispatcher = get_class('customer.utils', 'Dispatcher')
CommunicationEventType = get_model('customer', 'CommunicationEventType')


def email(request):
    contact_flatpage = get_object_or_404(FlatPage, url='/help/contacts/')
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            code = 'CONTACT_FORM'
            ctx = form.cleaned_data
            try:
                event_type = CommunicationEventType.objects.get(code=code)
            except CommunicationEventType.DoesNotExist:
                # No event-type in database, attempt to find templates for this
                # type and render them immediately to get the messages.  Since we
                # have not CommunicationEventType to link to, we can't create a
                # CommunicationEvent instance.
                templates = CommunicationEventType.objects.get_and_render(code, ctx)
                event_type = None
            else:
                templates = event_type.get_messages(ctx)
            Dispatcher().dispatch_direct_messages(CONTACT_FORM_BCC, templates)
            messages.success(request, 'Ваше сообщение успешно отрпавлено')
    else:
        form = ContactForm()
    return render(request, 'flatpages/default.html', {
        "form": form,
        "flatpage": contact_flatpage,
        })