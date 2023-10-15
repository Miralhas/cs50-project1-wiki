from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.urls import reverse
from markdown2 import markdown
from django import forms
from random import choice
from . import util


class NewSearchForms(forms.Form):
    search_content = forms.CharField(
        label=False, 
        widget=forms.TextInput(attrs={
            "placeholder": "Search Encyclopedia",
            "class": "search"
        })
    )

class NewWikiForms(forms.Form):
    wiki_title = forms.CharField(label=False, widget=forms.TextInput())
    wiki_content = forms.CharField(label=False, widget=forms.Textarea())

class UpdateWikiForms(forms.Form):
    wiki_title = forms.CharField(label=False)
    wiki_content = forms.CharField(label=False, widget=forms.Textarea())


def index(request):
    return render(
        request,
        "encyclopedia/index.html",
        context={"entries": util.list_entries()},
    )

def wiki_page(request, title):
    if title not in util.list_entries():
        pages = []
        for wiki_page in util.list_entries():
            x = f"{wiki_page}, {wiki_page.lower()}, {wiki_page.upper()}"
            if title in x:
                pages.append(wiki_page)
        return render(request, "encyclopedia/search.html", context={
            "wiki_pages": pages
        })

    return render(request,"encyclopedia/wiki_page.html", context={
                    "title": title,
                    "markdown": markdown(util.get_entry(title))
                })

def search(request):
    if request.method == "GET":
        form = NewSearchForms(request.GET)
        if form.is_valid():
            search_content = form.cleaned_data["search_content"]
            return wiki_page(request, search_content)
        
def add_wiki(request):
    if request.method == "POST":
        form = NewWikiForms(request.POST)
        print(form)
        if form.is_valid():
            wiki_title = form.cleaned_data["wiki_title"]
            wiki_content = form.cleaned_data["wiki_content"]
            if wiki_title in util.list_entries():
                return HttpResponse("Error! Wiki already Exists")
            else:
                util.save_entry(wiki_title, wiki_content)
                return HttpResponseRedirect(reverse("wiki:index"))
            
    return render(request, "encyclopedia/new_wiki.html", context={
        "form": NewWikiForms(),
    })


def update_wiki(request, title):
    if request.method == "POST":
        wiki_title = request.POST.get("wiki_title")
        wiki_content = request.POST.get("wiki_content")
        print(wiki_title, wiki_content)
        util.save_entry(wiki_title, wiki_content)
        return HttpResponseRedirect(reverse("wiki:index"))

    return render(request, "encyclopedia/update_wiki.html", context={
        "title": title,
        "content": util.get_entry(title),
    })

def random_wiki(request):
    title = choice(util.list_entries())
    return wiki_page(request, title)