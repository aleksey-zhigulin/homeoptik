# -*- coding: utf-8 -*-
__author__ = 'aleksey'

from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ваше имя - обязательно'}), required=True)
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Ваш Email - обязательно'}), required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 8,  'placeholder': 'Сообщение...'}), required=True)

