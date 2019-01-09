from django.shortcuts import render
from forms import QueryForm
from . import utils


def list_tweets(request):
    if request.method == 'POST':
        form = QueryForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = QueryForm()
    return render(request, 'results.html', {'form': form})
