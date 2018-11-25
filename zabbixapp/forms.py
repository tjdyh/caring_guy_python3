from django import forms
from pprint import pprint


class AddForm(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()