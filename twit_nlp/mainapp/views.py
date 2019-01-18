from django.shortcuts import render, redirect
from .forms import TwitterForm, StatsForm
from .utils import get_tweets_data, get_query_results


def get_twitter_sentiment(request):
    if request.method == 'POST':
        form = TwitterForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            num_of_tweets = form.cleaned_data['num_of_tweets']
            tweets_data = get_tweets_data(get_query_results(query, num_of_tweets))
            return render(request, 'results_sentiment.html', {'tweets_data': tweets_data})
    else:
        form = TwitterForm()
    return render(request, 'sentiment.html', {'form': form})

def get_stats(request):
    if request.method == 'POST':
        form = StatsForm(request.POST)
        if form.is_valid():
            something = form.cleaned_data['num_of_something']
            return render(request, 'results_stats.html', {'something': something})
    else:
        form = StatsForm()
    return render(request, 'stats.html', {'form': form})
