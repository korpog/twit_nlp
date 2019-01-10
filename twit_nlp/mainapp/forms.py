from django import forms

class QueryForm(forms.Form):
    query = forms.CharField(label='Twitter query', max_length=120)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['query'].widget.attrs.update(
            {'class': 'form-control'})