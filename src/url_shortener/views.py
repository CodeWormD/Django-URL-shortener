from django.shortcuts import redirect, render

from .models import Link


def create(request):
    if request.method == 'POST':
        geturl = request.POST.get('url')
        obj = Link.create(link=geturl)
        context = {         
            'url': obj.url,
            'shorturl': request.get_host() + '/s/' + obj.shorturl
        }
        return render(request, 'shortener.html', context)
    else:
        return render(request, 'shortener.html')

def redir(request, link):
    try:
        obj = Link.objects.get(shorturl=link)
        return redirect(obj.url)
    except:
        obj = None

    return redirect(create)
    