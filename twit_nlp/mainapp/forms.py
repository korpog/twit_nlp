from django import forms

class QueryForm(forms.Form):
    query = forms.CharField(label='Twitter query', max_length=120)