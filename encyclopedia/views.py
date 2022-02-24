#from urllib.request import HTTPRedirectHandler
#from django.shortcuts import render
#from . import util
import os
import random
from django.http import HttpResponseRedirect

from django.shortcuts import redirect

from django.urls import reverse

from django.core.files.base import ContentFile

from django.shortcuts import render
from django import forms

from .forms import EntryForm
from .forms import EditForm

from .models import Entry
from .models import Edit

from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, title):
    info = util.get_entry(title,"True")
    if info:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "info": info
            })
    else:
        return render(request, "encyclopedia/404.html", {
            "title": title
            })

def randompage(request):
    entry = random.choice(util.list_entries()) #list of wikis
    info = util.get_entry(entry, "True")
    return render(request, "encyclopedia/entry.html", {
       "title":entry,
        "info":info
   })

# def random_page(request):
#    ventries = util.list_entries()
#    selected_page = random.choice(entries)
#    return HttpResponseRedirect(reverse('wiki', args=[selected_page]))

def search(request):
    search = request.GET.get('q')
    info = util.get_entry(search, "True")
    if info:
        return render(request, "encyclopedia/entry.html", {
            "title": search,
            "info": info
        })
    else:
        names = []
        for entry in util.list_entries():
            if entry.lower().find(search.lower()) != -1:
                names.append(entry)
        if names:
            return render(request, "encyclopedia/results.html", {
                        "title": search,
                        "entries": names 
                    })
        else:
            return render(request, "encyclopedia/404.html", {
                "title": search
            })

def edit(request, title):
    if request.method == "GET":
        info = util.get_entry(title, False)
        data = {
            'Body': info
        }
        form = EditForm(initial = data)
        return render(request, "encyclopedia/edit.html", {
            'title': title,
            'form': form
        })
    else: 
        form = EditForm(request.POST)
        if form.is_valid():
            body = form.cleaned_data['Body']
            util.save_entry(title, body)
            return redirect('title', title=title)
 
def newpage(request):
    if request.method == "POST":
        form = EntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            Body = form.cleaned_data['Body']
            full_filename=os.path.join('entries', title+'.md')
            if os.path.isfile(full_filename):
                return render(request, "encyclopedia/conflicterror.html", {
                    'title': title
                })
            fout = open(full_filename, 'wt')
            fout.write(Body)
            fout.close()
            return redirect('title', title=title)

    else:
        return render(request, "encyclopedia/newpage.html", {
            'form': EntryForm()
        })