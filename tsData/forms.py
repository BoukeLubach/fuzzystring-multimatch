from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset


class FilterForm(forms.Form):
    searchInput = forms.CharField(label='', 
                                required=False,
                                widget=forms.TextInput(
                                attrs={'placeholder': 'Search....'}))
    filter_threshold = forms.IntegerField(label='Match threshold')