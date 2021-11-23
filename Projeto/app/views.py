from django.db.models.functions import Concat
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import RegisterUser, AddPublication, AddComment
from django.contrib.auth import login
from django.contrib import messages
from django.db.models import Value as V
from app.models import Publications, Publication_status, Users, Publication_topics, Comments, Favorites, Groups
from app.forms import SearchPubForm, SearchUsersForm
from datetime import *

def register_request(request):
    if request.method == "POST":
        form = RegisterUser(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("../")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = RegisterUser()
    return render(request=request, template_name="register.html", context={"register_form" : form})

def index(request):
    return redirect("publications")

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
            categoria=categoria.description
            if title and content and categoria:
                if user.group.description == "Gestor" or user.group.description == "Admin":
                    status = Publication_status.objects.get(description__exact="Aprovado")
                else:
                    status = Publication_status.objects.get(description__exact="Por Aprovar")
                cats= Publication_topics.objects.all()
                for cat in cats:
                    if categoria == cat.description:
                        topic = Publication_topics.objects.get(description__exact=categoria)
                        print("escolhido")
                        break
                p = Publications.objects.create(title=title, content=content, author=user, status=status, topic=topic)
                p.save()
                print(p)
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

def publication(request, pub_id):
    #  pub_id = request.GET['pub_id']
    # pub_id = 1
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
                control = False
                favoritos = Favorites.objects.all()
                for fav in favoritos:
                    if fav.publication == pub and fav.author == user:
                        control = True
                        break
                if pub.status.description == "Aprovado" or user.group.description == "Gestor" or user.group.description == "Admin":
                    return render(request, 'publication.html', {"pub": pub, "comments": ret_coms, "form": form,"user":user, 'error': error,"control":control})
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
                control=False
                favoritos = Favorites.objects.all()
                for fav in favoritos:
                    if fav.publication == pub and fav.author == user:
                        control = True
                        break
                return render(request, 'publication.html', {"pub": pub, "comments": ret_coms, "form": form,"user":user,"control":control})

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
        elif  "add_favorito" in  request.POST.keys():
            id = request.POST["add_favorito"]
            pub = Publications.objects.get(id__exact=id)
            fav = Favorites()
            fav.publication=pub
            fav.author=user
            fav.save()
            ret = "/publication/" + str(pub_id)
            return redirect(ret)
        elif "tirar_favorito" in  request.POST.keys():
            id = request.POST["tirar_favorito"]
            pub = Publications.objects.get(id__exact=id)

            fav = Favorites.objects.get(author__exact=user, publication__exact=pub)
            fav.delete()
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
        control=False


        if request.user.is_authenticated:
            user = Users.objects.get(username__exact=request.user.username)
            favoritos = Favorites.objects.all()
            for fav in favoritos:
                if fav.publication == pub and fav.author == user:
                    control=True
                    break
            
        if pub.status.description =="Aprovado" or (user is not None and (user.group.description == 'Gestor' or user.group.description == 'Admin')):
            return render(request, 'publication.html', {"pub":pub,"comments":ret_coms,"form":form,"user":user,"control":control})
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
    if user.group.description != "Gestor" and user.group.description != "Admin":
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

    if not request.user.is_authenticated:
        return redirect('/login')
    user = Users.objects.get(username__exact=request.user.username)
    if user.group.description != "Gestor" and user.group.description != "Admin":
        return redirect('/publications')

    if request.method == 'POST':

        if 'Filtro' in request.POST:

            form = SearchUsersForm(request.POST)

            if form.is_valid():

                username = form.cleaned_data['username']
                fullname = form.cleaned_data['fullname']
                group = form.cleaned_data['group']

                users = Users.objects.all()
                if username:
                    users = users.filter(username__contains=username)
                if group:
                    users = users.filter(group__description__exact=group)
                if fullname:
                    users = users.annotate(full_name=Concat('first_name', V(' '), 'last_name')). \
                        filter(full_name__contains=fullname)

                ret_users = []
                for u in users:
                    if user.group.description == 'Admin':
                        ret_users.append(u)
                    elif user.group.description == 'Gestor' and u.group.description != 'Gestor' and u.group.description != 'Admin':
                        ret_users.append(u)


            else:
                form = SearchUsersForm()
                users = Users.objects.all()
                ret_users = []
                for u in users:
                    if user.group.description == 'Admin':
                        ret_users.append(u)
                    elif user.group.description == 'Gestor' and u.group.description != 'Gestor' and u.group.description != 'Admin':
                        ret_users.append(u)

        elif 'group' in request.POST:

            username = request.POST.get('user')
            group = request.POST.get('group')

            grupo = Groups.objects.get(description__exact=group)

            change_user = Users.objects.get(username__exact=username)
            change_user.group = grupo
            change_user.save()

            form = SearchUsersForm()
            users = Users.objects.all()
            ret_users = []
            for u in users:
                if user.group.description == 'Admin':
                    ret_users.append(u)
                elif user.group.description == 'Gestor' and u.group.description != 'Gestor' and u.group.description != 'Admin':
                    ret_users.append(u)


    else:

        form = SearchUsersForm()
        users = Users.objects.all()
        ret_users = []
        for u in users:
            if request.user.username == 'admin':
                ret_users.append(u)
            elif user.group.description == 'Gestor' and u.group.description != 'Gestor' and u.group.description != 'Admin':
                ret_users.append(u)


    groups = Groups.objects.all()
    if request.user.is_authenticated:
        user = Users.objects.get(username__exact=request.user.username)
        print(user.group)
        return render(request, 'manage_users.html', {'user' : user, 'ret_users': ret_users, 'form' : form, 'groups': groups})
    else:
        return render(request, 'manage_users.html', {'ret_users': ret_users, 'form' : form, 'groups': groups})


def publicationsArquivadas(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    user = Users.objects.get(username__exact=request.user.username)
    if user.group.description != "Gestor" and user.group.description != "Admin":
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

def favoritos(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    user = Users.objects.get(username__exact=request.user.username)

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
            ret_pubs=[]
            favoritos = Favorites.objects.all()
            for favorito in favoritos:
                if favorito.author.username == user.username  and favorito.publication in pubs:
                    ret_pubs.append(favorito.publication)
        else:
            form = SearchPubForm()
            pubs = Publications.objects.all()
            ret_pubs = []
            favoritos = Favorites.objects.all()
            for favorito in favoritos:
                if favorito.author.username == user.username:
                    ret_pubs.append(favorito.publication)
    else:
        form = SearchPubForm()
        pubs = Publications.objects.all()
        ret_pubs = []
        favoritos= Favorites.objects.all()
        for favorito in favoritos:
            if favorito.author.username ==user.username :
                ret_pubs.append(favorito.publication)

    if request.user.is_authenticated:
        user = Users.objects.get(username__exact=request.user.username)
        print(user.group)
        return render(request, 'favoritos.html', {'user': user, 'pubs_aproved': ret_pubs, 'form': form})
    else:
        return render(request, 'favoritos.html', {'pubs_aproved': ret_pubs, 'form': form})

def topic(request):
    if not request.user.is_authenticated:
        return redirect('/login')
    user = Users.objects.get(username__exact=request.user.username)
    if user.group.description != "Gestor" and user.group.description != "Admin":
        return redirect('/publications')
    if  request.POST:
        if "topic_des" in request.POST:
            print("entrei")
            id = request.POST["topic_id"]
            des= request.POST["topic_des"]
            if Publication_topics.objects.filter(description__exact=des).exists():
                pass
            else:
                topics=Publication_topics.objects.get(id__exact=id)
                topics.description=des
                topics.save()

        elif "new_topic" in request.POST:
            new_topic= request.POST["new_topic"]
            if Publication_topics.objects.filter(description__exact=new_topic).exists():
                pass
            else:
                topics= Publication_topics.objects.create(description=new_topic)
                topics.save()


    topics = Publication_topics.objects.all()
    print(topics)
    return render(request,'topic.html',{'user':user,"topics":topics})

