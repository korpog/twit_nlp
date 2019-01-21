from django import forms


class TwitterForm(forms.Form):
    RESULT_CHOICES = (
        ('rec', 'recent'),
        ('mix', 'mixed'),
        ('pop', 'popular')
    )
    query = forms.CharField(label='Twitter query', max_length=120)
    num_of_tweets = forms.IntegerField(
        label="Number of tweets", min_value=1, max_value=15)
    result_type = forms.ChoiceField(
        label="Result type", choices=RESULT_CHOICES)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['query'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Enter query here'})
        self.fields['num_of_tweets'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['result_type'].widget.attrs.update(
            {'class': 'form-control'})


class StatsForm(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your message goes here'}))
    num_of_something = forms.IntegerField(
        label="Number of tweets", min_value=1, max_value=15)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['num_of_something'].widget.attrs.update(
            {'class': 'form-control'})
