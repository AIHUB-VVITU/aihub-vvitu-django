from django.shortcuts import render
from django.http import Http404

# Create your views here.
def play_game(request, id):
    if '..' in id or id.startswith('/'):
        raise Http404
    template_name = f'{id}.html'
    return render(request, template_name)