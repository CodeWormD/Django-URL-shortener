from django.shortcuts import render, redirect
from django.http import HttpResponse
import uuid
from django.views.decorators.http import require_http_methods
from .forms import UrlForm
from .models import Link


def create(request):
    form = UrlForm(request.POST or None)
    if request.method == 'POST':
        geturl = request.POST.get('url')
        obj = Link.create(link=geturl)
        return render(request, 'shortener.html', context = {
            'form': form,            
            'url': obj.url,
            'shorturl': request.get_host() + '/s/' + obj.shorturl
        })
    else:
        return render(request, 'shortener.html', context = {
                        'form': form,})

def redir(request, link):
    form = UrlForm(request.POST or None)
    try:
        obj = Link.objects.get(shorturl=link)
        return redirect(obj.url)
    except:
        obj = None

    return redirect(create)
    