from django.db.models.functions import Concat
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import RegisterUser, AddPublication, AddComment
from django.contrib.auth import login
from django.contrib import messages
from django.db.models import Value as V
from app.models import Publications, Publication_status, Users, Publication_topics, Comments
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
    # só pode ir para esta página se o utilizador estiver logado
    # DUVIDA : Como fazer redirect de volta
    if not request.user.is_authenticated:
        return redirect('/login')
    user=Users.objects.get(username__exact=request.user.username)
    if user.group.description == "Leitor":
        return redirect('/publications')

    if request.method == "POST":
        form = AddPublication(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            content=content.strip()
            content=content[3:-4]
            categoria=form.cleaned_data['categoria']
            if title and content and categoria:
                if user.group.description == "Gestor":
                    status = Publication_status.objects.get(description__exact="Aprovado")
                else:
                    status = Publication_status.objects.get(description__exact="Por Aprovar")
                cats= Publication_topics.objects.all()
                control=False
                for cat in cats:
                    if categoria == cat.description:
                        control=True
                        topic = Publication_topics.objects.get(description__exact=categoria)
                        break
                if not control:
                    topic=Publication_topics.objects.create(description=categoria)
                    topic.save()
                    topic=Publication_topics.objects.get(description__exact=categoria)
                p = Publications.objects.create(title=title, content=content, author=user, status=status, topic=topic)
                p.save()
                return redirect('/publications')
            else:
                form = AddPublication()
                return render(request, 'insert.html', {'form': form})
        else:
            form = AddPublication()
            return render(request, 'insert.html', {'form': form})

    form =AddPublication()
    return render(request, 'insert.html',{'form' : form})


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
                pubs = pubs.annotate(full_name=Concat('author__first_name', V(' '), 'author__last_name')). \
                    filter(full_name__contains=author)
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

    if request.method == 'POST' and request.user.is_authenticated:
        form = AddComment(request.POST)
        user = Users.objects.get(username__exact=request.user.username)
        print(request.POST)
        #adicionar o comentário AQUI E DONE
        if form.is_valid():
            content = form.cleaned_data['content']
            form.cleaned_data['content'] = ""

            if 'comment' in request.session and request.session['comment'] == content:
                error = True
                form = AddComment()
                pub = Publications.objects.get(id__exact=pub_id)
                comments = Comments.objects.all()
                ret_coms = []
                for comment in comments:
                    if comment.publication.id == pub_id:
                        ret_coms.append(comment)
                user = Users.objects.get(username__exact=request.user.username)
                if pub.status.description == "Aprovado" or user.group.description == 'Gestor':
                    return render(request, 'publication.html', {"pub": pub, "comments": ret_coms, "form": form,"user":user, 'error': error})
                return redirect('/publications')

            else:
                request.session['comment'] = content
                pub=Publications.objects.get(id__exact=pub_id)
                comentario = Comments.objects.create(comment=content,author=user,publication=pub)
                comentario.save()
                pub = Publications.objects.get(id__exact=pub_id)
                comments = Comments.objects.all()
                ret_coms = []
                for comment in comments:
                    if comment.publication.id == pub_id:
                        ret_coms.append(comment)
                form = AddComment()
                return render(request, 'publication.html', {"pub": pub, "comments": ret_coms, "form": form,"user":user})

        elif "comment_id" in  request.POST.keys() :
            id = request.POST["comment_id"]

            com = Comments.objects.get(id__exact=id)
            com.delete()
            ret = "/publication/" + str(pub_id)
            return redirect(ret)
        elif "publication_aprov_id" in  request.POST.keys() :
            id = request.POST["publication_aprov_id"]
            pub = Publications.objects.get(id__exact=id)
            status = Publication_status.objects.get(description__exact="Aprovado")
            pub.status = status
            pub.save()
            ret = "/publication/" + str(pub_id)
            return redirect(ret)
        elif  "publication_arqu_id" in  request.POST.keys():
            id = request.POST["publication_arqu_id"]
            pub = Publications.objects.get(id__exact=id)
            status = Publication_status.objects.get(description__exact="Arquivado")
            pub.status = status
            pub.save()
            ret = "/publication/" + str(pub_id)
            return redirect(ret)
        elif  "publication_arquivar" in  request.POST.keys():
            id = request.POST["publication_arquivar"]
            pub = Publications.objects.get(id__exact=id)
            status = Publication_status.objects.get(description__exact="Arquivado")
            pub.status = status
            pub.save()
            ret = "/publication/" + str(pub_id)
            return redirect(ret)

    else:
        form = AddComment()
        pub = Publications.objects.get(id__exact=pub_id)
        comments = Comments.objects.all()
        ret_coms=[]
        for comment in comments:
            if comment.publication.id == pub_id:
                ret_coms.append(comment)
        user = None
        if request.user.is_authenticated:
            user = Users.objects.get(username__exact=request.user.username)
        if pub.status.description =="Aprovado" or (user is not None and user.group.description == 'Gestor'):
            return render(request, 'publication.html', {"pub":pub,"comments":ret_coms,"form":form,"user":user})
        return redirect('/publications')

def my_publications(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    user=Users.objects.get(username__exact=request.user.username)
    if user.group.description == "Leitor":
        return redirect('/publications')
    if request.method == 'POST':
        form = SearchPubForm(request.POST)

        if form.is_valid():

            title = form.cleaned_data['title']
            date = form.cleaned_data['date']
            topic = form.cleaned_data['topic']

            pubs = Publications.objects.all()
            if title:
                pubs = pubs.filter(title__contains=title)
            if date:
                pubs = pubs.filter(created_on__date=date)
            if topic:
                pubs = pubs.filter(topic__exact=topic)

            ret_pubs = []
            approval_pubs = []
            arquivadas_pubs = []
            for pub in pubs:
                # depois podemos ver se adicionamos as por aprovar ou metemos um select com o status das publications
                if pub.status.description == "Aprovado" and pub.author.username == user.username:
                    ret_pubs.append(pub)
                elif pub.status.description == "Por Aprovar" and pub.author.username == user.username:
                    approval_pubs.append(pub)
                elif pub.status.description == "Arquivadas" and pub.author.username == user.username:
                    arquivadas_pubs.append(pub)



        else:
            form = SearchPubForm()
            pubs = Publications.objects.all()
            ret_pubs = []
            approval_pubs = []
            arquivadas_pubs = []
            for pub in pubs:
                # depois podemos ver se adicionamos as por aprovar ou metemos um select com o status das publications
                if pub.status.description == "Aprovado" and pub.author.username == user.username:
                    ret_pubs.append(pub)
                elif pub.status.description == "Por Aprovar" and pub.author.username == user.username:
                    approval_pubs.append(pub)
                elif pub.status.description == "Arquivadas" and pub.author.username == user.username:
                    arquivadas_pubs.append(pub)

    else:
        form = SearchPubForm()
        pubs = Publications.objects.all()
        ret_pubs = []
        approval_pubs = []
        arquivadas_pubs = []
        for pub in pubs:
            # depois podemos ver se adicionamos as por aprovar ou metemos um select com o status das publications
            if pub.status.description == "Aprovado" and pub.author.username == user.username:
                ret_pubs.append(pub)
            elif pub.status.description == "Por Aprovar" and pub.author.username == user.username:
                approval_pubs.append(pub)
            elif pub.status.description == "Arquivadas" and pub.author.username == user.username:
                arquivadas_pubs.append(pub)

    if request.user.is_authenticated:
        user = Users.objects.get(username__exact=request.user.username)
        print(user.group)
        return render(request, 'my_pubs.html', {'user' : user, 'pubs_aproved': ret_pubs, 'pubs_aproval': approval_pubs, 'pubs_arquivadas': arquivadas_pubs, 'form' : form})
    else:
        return render(request, 'my_pubs.html', {'pubs_aproved': ret_pubs, 'pubs_aproval': approval_pubs, 'pubs_arquivadas': arquivadas_pubs, 'form' : form})


def pendent_publications(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    user = Users.objects.get(username__exact=request.user.username)
    if user.group.description != "Gestor":
        return redirect('/publications')
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
                pubs = pubs.annotate(full_name=Concat('author__first_name', V(' '), 'author__last_name')). \
                    filter(full_name__contains=author)
            if topic:
                pubs = pubs.filter(topic__exact=topic)

            ret_pubs = []
            for pub in pubs:
                if pub.status.description == "Por Aprovar" :
                    ret_pubs.append(pub)
        else:
            form = SearchPubForm()
            pubs = Publications.objects.all()
            ret_pubs = []
            for pub in pubs:
                if pub.status.description == "Por Aprovar" :
                    ret_pubs.append(pub)

    else:
        form = SearchPubForm()
        pubs = Publications.objects.all()
        ret_pubs = []
        for pub in pubs:
            if pub.status.description == "Por Aprovar" :
                ret_pubs.append(pub)

    if request.user.is_authenticated:
        user = Users.objects.get(username__exact=request.user.username)
        print(user.group)
        return render(request, 'pendent_pubs.html', {'user': user, 'pubs_aproved': ret_pubs, 'form': form})
    else:
        return render(request, 'pendent_pubs.html', {'pubs_aproved': ret_pubs, 'form': form})

def manage_users(request):
    return render(request, 'login.html')

def publicationsArquivadas(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    user = Users.objects.get(username__exact=request.user.username)
    if user.group.description != "Gestor":
        return redirect('/publications')
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
                pubs = pubs.annotate(full_name=Concat('author__first_name', V(' '), 'author__last_name')). \
                    filter(full_name__contains=author)
            if topic:
                pubs = pubs.filter(topic__exact=topic)

            ret_pubs = []
            for pub in pubs:
                if pub.status.description == "Arquivado":
                    ret_pubs.append(pub)
        else:
            form = SearchPubForm()
            pubs = Publications.objects.all()
            ret_pubs = []
            for pub in pubs:
                if pub.status.description == "Arquivado":
                    ret_pubs.append(pub)

    else:
        form = SearchPubForm()
        pubs = Publications.objects.all()
        ret_pubs = []
        for pub in pubs:
            if pub.status.description == "Arquivado":
                ret_pubs.append(pub)

    if request.user.is_authenticated:
        user = Users.objects.get(username__exact=request.user.username)
        print(user.group)
        return render(request, 'pendent_pubs.html', {'user': user, 'pubs_aproved': ret_pubs, 'form': form})
    else:
        return render(request, 'pendent_pubs.html', {'pubs_aproved': ret_pubs, 'form': form})

def removeCommment(request):
    print(request.POST['comment_id'])
