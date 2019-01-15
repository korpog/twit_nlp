from django.shortcuts import render, redirect
from .forms import QueryForm
from .utils import get_tweets_data, get_query_results


def list_tweets(request):
    if request.method == 'POST':
        form = QueryForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            tweets_data = get_tweets_data(get_query_results(query))
            return render(request, 'results.html', {'tweets_data': tweets_data})
    else:
        form = QueryForm()
    return render(request, 'index.html', {'form': form})
