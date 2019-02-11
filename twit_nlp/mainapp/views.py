from django.shortcuts import render, redirect
from django.views.generic import FormView
from .forms import TwitterForm, StatsForm
from .utils import get_tweets_data, get_query_results

class TwitterFormView(FormView):
    form_class = TwitterForm
    template_name = "index.html"

    def form_valid(self, form):
            query = form.cleaned_data['query']
            num_of_tweets = form.cleaned_data['num_of_tweets']
            result_type = form.cleaned_data['result_type']
            tweets_data = get_tweets_data(get_query_results(query, num_of_tweets, result_type))
            return render(self.request, 'results_sentiment.html', {'tweets_data': tweets_data})
