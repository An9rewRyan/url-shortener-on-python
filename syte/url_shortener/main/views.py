from django.http.response import HttpResponse
from django.shortcuts import render
from .forms import SearchForm
from main.models import Link
from shortener import main
from django.shortcuts import redirect

def index(request):

    _SearchForm = SearchForm()
    context = {'search_form': _SearchForm}

    return render (request, "main/index.html", context)

def shorten(request):

    shortLink = ''

    if request.method == "POST":

        longLink = request.POST.get("request")

        link = Link.objects.filter(longLink = longLink)

        if link.exists():
            link = Link.objects.get(longLink = longLink)
            context = {'shortLink':'http://127.0.0.1:8000/main/'+str(link.hash), 'longLink':link.longLink}
            return render (request,"main/result.html", context)

        else:
            hash = main.shorten(longLink)
            shortLink = 'http://127.0.0.1:8000/main/' + str(hash)

            if shortLink != 'http://127.0.0.1:8000/main/' + str(0):
                newLinkObj = Link(longLink = longLink, hash = hash)
                newLinkObj.save()
                context = {'shortLink':shortLink, 'longLink':longLink}
                return render (request,"main/result.html", context)
            else:
                return HttpResponse ('Bad url.')

def redirect_(request, hash):

    link = Link.objects.get(hash = hash)
    link.clicks = link.clicks + 1
    return redirect(link.longLink)