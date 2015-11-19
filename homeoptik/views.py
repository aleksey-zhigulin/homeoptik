from forked.flatpages.models import FlatPage
from django.shortcuts import render, get_object_or_404

from forms import ContactForm

def email(request):
    contact_flatpage = get_object_or_404(FlatPage, url='/help/contacts/')
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = ContactForm()
    return render(request, 'flatpages/default.html', {
        "form": form,
        "flatpage": contact_flatpage,
    })