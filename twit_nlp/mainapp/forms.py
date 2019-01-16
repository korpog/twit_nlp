from django import forms


class QueryForm(forms.Form):
    query = forms.CharField(label='Twitter query', max_length=120)
    num_of_tweets = forms.IntegerField(
        label="Number of tweets", min_value=1, max_value=15)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['query'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Enter query here'})
        self.fields['num_of_tweets'].widget.attrs.update(
            {'class': 'form-control'})
