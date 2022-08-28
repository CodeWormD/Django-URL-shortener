from django.shortcuts import render
from django.http import HttpResponse
import uuid
from django.views.decorators.http import require_http_methods
from .forms import UrlForm
from .models import Link


def create(request):
    form = UrlForm(request.POST or None)
    url = request.POST['url']
    short = str(uuid.uuid4())[:10]
    
    context = {
        'form': form
    }
    
    if form.is_valid():
        form.save(commit=False)
        model = Link.objects.create(url=url, shorturl=short)
        model.save()
        return render(request, 'shortener.html', context)

    
    


    
    


# if not form.is_valid():
#     return HttpResponse('Form is not valid')