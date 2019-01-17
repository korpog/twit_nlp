from django.shortcuts import render, redirect
from .forms import QueryForm
from .utils import get_tweets_data, get_query_results


def analyse_tweets(request):
    if request.method == 'POST':
        form = QueryForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            num_of_tweets = form.cleaned_data['num_of_tweets']
            tweets_data = get_tweets_data(get_query_results(query, num_of_tweets))
            return render(request, 'results_sentiment.html', {'tweets_data': tweets_data})
    else:
        form = QueryForm()
    return render(request, 'sentiment.html', {'form': form})
