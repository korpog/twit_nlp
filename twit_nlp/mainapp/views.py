from django.shortcuts import render, redirect
from .forms import QueryForm
from .utils import tweets_to_dict, get_query_results


def list_tweets(request):
    if request.method == 'POST':
        form = QueryForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            tweets_dict = tweets_to_dict(get_query_results(query))
            return render('results', {'tweets_dict': tweets_dict})
    else:
        form = QueryForm()
    return render(request, 'index.html', {'form': form})
