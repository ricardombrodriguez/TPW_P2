from django.db.models.functions import Concat
from django.shortcuts import render, redirect
from .forms import RegisterUser
from django.contrib.auth import login
from django.contrib import messages
from app.models import Publications, Publication_status, Users, Publication_topics
from app.forms import SearchPubForm
from datetime import *

def register_request(request):
    if request.method == "POST":
        form = RegisterUser(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("login.html")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = RegisterUser()
    return render(request=request, template_name="register.html", context={"register_form" : form})

def insert_pub(request):
    if 'title' and 'content' in request.POST:
        title = request.POST['title']
        content = request.POST['content']
        if title and content:
            status = Publication_status.objects.get(description__exact="Por Aprovar")
            topic = Publication_topics.objects.get(description__exact="Cultura")
            user = Users.objects.get(username__exact=request.user.username)
            p = Publications.objects.create(title=title, content=content, author=user, status=status, topic=topic)
            p.save()

    return render(request, 'insert.html')


def publications(request):

    if request.method == 'POST':

        form = SearchPubForm(request.POST)

        if form.is_valid():

            title = form.cleaned_data['title']
            date = form.cleaned_data['date']
            author = form.cleaned_data['author']
            topic = form.cleaned_data['topic']

            pubs = Publications.objects.all()
            if title:
                pubs = pubs.filter(title__contains=title)
            if date:
                pubs = pubs.filter(created_on__date=date)
            if author:
                pubs = pubs.filter(author__full_name__contains=author)
            if topic:
                pubs = pubs.filter(topic__exact=topic)

            ret_pubs = []
            for pub in pubs:
                if pub.status.description == "Aprovado":
                    ret_pubs.append(pub)


        else:
            form = SearchPubForm()
            pubs = Publications.objects.all()
            ret_pubs = []
            for pub in pubs:
                if pub.status.description == "Aprovado":
                    ret_pubs.append(pub)


    else:
        form = SearchPubForm()
        pubs = Publications.objects.all()
        ret_pubs = []
        for pub in pubs:
            if pub.status.description == "Aprovado":
                ret_pubs.append(pub)

    if request.user.is_authenticated:
        user = Users.objects.get(username__exact=request.user.username)
        print(user.group)
        return render(request, 'publications.html', {'user' : user, 'pubs_aproved': ret_pubs, 'form' : form})
    else:
        return render(request, 'publications.html', {'pubs_aproved': ret_pubs, 'form' : form})

def publication(request,pub_id):
    return render(request, 'publication.html')

def my_publications(request):
    return render(request, 'login.html')

def pendent_publications(request):
    return render(request, 'login.html')

def manage_users(request):
    return render(request, 'login.html')