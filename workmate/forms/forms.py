# -*- coding: utf-8 -*-
from django import forms

from ..models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['tags'].widget.attrs['class'] = 'search dropdown'
