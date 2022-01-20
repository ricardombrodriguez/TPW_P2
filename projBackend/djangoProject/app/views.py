from django.shortcuts import render
from django.db.models.functions import Concat
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.db.models import Value as V
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from app.models import Groups, Users, Publication_status, Publication_topics, Publications, Comments, Favorites
from app.serializers import GroupsSerializer, UsersSerializer, PublicationStatusSerializer, \
    PublicationTopicsSerializer, PublicationsSerializer, CommentsSerializer, FavoritesSerializer, UserSerializer, TokenSerializer


# Create your views here.
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


# Métodos do Groups
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_group(request):
    groups = Groups.objects.all()

    # PROVAVELMENTE VAI SER PRECISO DIZER QUEM PEDIU PARA SABER QUE GRUPOS LHE MANDAR

    serializer = GroupsSerializer(groups, many=True)
    return Response(serializer.data)


# Métodos do User
@api_view(['POST'])
def create_user(request):
    print(request.data)
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        ret = serializer.create(request.data)
        token = TokenSerializer(data={'key': ret.key})
        return Response(token.initial_data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_user(request):
    id = request.data['id']
    try:
        user = Users.objects.get(id=id)
    except Users.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = UsersSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_users(request):
    users = Users.objects.all()
    # Devo precisar de saber quem me pediu para saber quantos lhe posso mostrar mas depois ponho isto
    # que agora ainda estou na fase de tentar meter tudo o que é preciso

    serializer = UsersSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_user(request):
    id = int(request.GET['id'])
    try:
        user = Users.objects.get(id=id)
    except Users.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = UsersSerializer(user)
    return Response(serializer.data)


# Apagar users'?????

##Publication Status
# Nao vai ter create nem delete so vai ter gets


@api_view(['GET'])
def pub_status_getALl(request):
    ret = Publication_status.objects.all()
    serializer = PublicationStatusSerializer(ret, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def pub_status_getOne(request):
    # Acho que é melhor fazer o get Pela descrição do que pelo id
    id = int(request.GET['id'])
    try:
        ret = Publication_status.objects.get(id=id)
    except Publication_status.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = PublicationStatusSerializer(status)
    return Response(serializer.data)


## Publication Topics
@api_view(['GET'])
def get_pub_topic(request):
    # Penso que faça mais sentido fazer o get pela descrição do que pelo id
    id = int(request.GET['id'])
    try:
        ret = Publication_topics.objects.get(id=id)
    except Publication_topics.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = PublicationTopicsSerializer(ret)
    return Response(serializer.data)


@api_view(['GET'])
def get_pub_topics(request):
    ret = Publication_topics.objects.all()
    serializer = PublicationTopicsSerializer(ret, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def get_pub_topics_create(request):
    serializer = PublicationTopicsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def get_pub_topics_update(request):
    # Não sei se vai ser pelo id se pela descrição, vou deixar pelo id e mais tarde troca-se se for preciso
    id = request.data['id']
    try:
        ret = Publication_topics.objects.get(id=id)
    except Publication_topics.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = PublicationTopicsSerializer(ret, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def get_pub_topics_delete(request, id):
    try:
        ret = Publication_topics.objects.get(id=id)
    except Publication_topics.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    ret.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


##PUBLICATION
@api_view(['GET'])
def pub(request):
    id = int(request.GET['id'])
    try:
        ret = Publications.objects.get(id=id)
    except Publications.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = PublicationsSerializer(ret)
    return Response(serializer.data)


@api_view(['GET'])
def pubs(request):
    ret = Publications.objects.all()
    serializer = PublicationsSerializer(ret, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def pubcreate(request):
    serializer = PublicationsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def pubupd(request):
    id = request.data['id']
    try:
        ret = Publications.objects.get(id=id)
    except Publications.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = PublicationsSerializer(ret, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




##COMMENTS
# NOS NO OUTRO PROJETO NÃO TINHAMOS O UPDATE DE UM COMENTÁRIO não sei se querem colocar ou não, se quiserem
# depois meto
@api_view(['GET'])
def comment(request):
    id = int(request.GET['id'])
    try:
        ret = Comments.objects.get(id=id)
    except Comments.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CommentsSerializer(ret)
    return Response(serializer.data)


@api_view(['GET'])
def comments(request):
    ret = Comments.objects.all()
    serializer = CommentsSerializer(ret, many=True)
    return Response(serializer.data)

#Código para obter os comentários de uma publicação
@api_view(['GET'])
def commentsPublication(request):
    id = int(request.GET['id'])  # ID DA PUBLICAÇÃO
    ret = Comments.objects.all()
    retorno = []
    for x in ret:
        if x.publication.id == id:
            retorno.append(x)
    serializer = CommentsSerializer(ret, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def commentcre(request):
    serializer = CommentsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def commentdel(request):
    id = int(request.GET['id'])
    try:
        ret = Comments.objects.get(id=id)
    except Comments.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    ret.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


## FAVORITOS
# Aqui não faz sentido ter updates, porque ou é favorito ou não é

@api_view(['GET'])
def fav(request):
    id = int(request.GET['id'])
    try:
        ret = Favorites.objects.get(id=id)
    except Favorites.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = FavoritesSerializer(ret)
    return Response(serializer.data)


@api_view(['GET'])
def favs(request):
    ret = Favorites.objects.all()
    serializer = FavoritesSerializer(ret, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def favcre(request):
    serializer = FavoritesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def favdel(request):
    id = int(request.GET['id'])
    pubs = int(request.GET['pub'])
    try:
        author=Users.objects.get(id=id)
        publication=Publications.objects.get(id=pubs)
        ret = Favorites.objects.get(author=author,publication=publication)
    except Favorites.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    ret.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def getAuthorPublications(request):
    id = int(request.GET['id'])
    try:
        autor = Users.objects.get(id=id)
    except Users.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    publications= Publications.objects.all()
    ret = []
    for publication in publications:
        if publication.author == autor:
            ret.append(publication)


    serializer = PublicationsSerializer(ret, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getAuthorPublicationsApproved(request):
    id = int(request.GET['id'])
    try:
        user = Users.objects.get(id=id)
    except Users.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    publications = Publications.objects.all()
    ret = []
    state = Publication_status.objects.get(description="Aprovado")
    for publication in publications:
        if publication.author == user and publication.status == state:
            ret.append(publication)

    serializer = PublicationsSerializer(ret, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getAuthorPublicationsPendent(request):
    id = int(request.GET['id'])
    try:
        autor = Users.objects.get(id=id)
    except Users.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    publications = Publications.objects.all()
    ret = []
    state = Publication_status.objects.get(description="Por Aprovar")
    for publication in publications:
        if publication.author == autor and publication.status == state:
            ret.append(publication)

    serializer = PublicationsSerializer(ret, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getPublicationsPendent(request):

    publications = Publications.objects.all()
    ret = []
    state = Publication_status.objects.get(description="Por Aprovar")
    for publication in publications:
        if publication.status == state:
            ret.append(publication)

    serializer = PublicationsSerializer(ret, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getPublicationsApproved(request):
    publications = Publications.objects.all()
    ret = []
    state = Publication_status.objects.get(description="Aprovado")
    for publication in publications:
        if publication.status == state:
            ret.append(publication)

    serializer = PublicationsSerializer(ret, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getSearchPublicationsApproved(request):
    author = (request.GET['author'])
    title = (request.GET['title'])
    date = (request.GET['date'])
    topic = (request.GET['topic'])
    pubs = Publications.objects.all()
    if title:
        pubs = pubs.filter(title__contains=title)
    if date:
        pubs = pubs.filter(created_on__date=date)
    if author:
        pubs = pubs.annotate(full_name=Concat('author__first_name', V(' '), 'author__last_name')). \
            filter(full_name__contains=author)
    if topic:
        pubs = pubs.filter(topic__description__exact=topic)
    ret = []
    state = Publication_status.objects.get(description="Aprovado")
    for publication in pubs:
        if publication.status == state:
            ret.append(publication)

    serializer = PublicationsSerializer(ret, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getSearchPublicationsPendent(request):
    author = (request.GET['author'])
    title = (request.GET['title'])
    date = (request.GET['date'])
    topic = (request.GET['topic'])
    pubs = Publications.objects.all()
    if title:
        pubs = pubs.filter(title__contains=title)
    if date:
        pubs = pubs.filter(created_on__date=date)
    if author:
        pubs = pubs.annotate(full_name=Concat('author__first_name', V(' '), 'author__last_name')). \
            filter(full_name__contains=author)
    if topic:
        pubs = pubs.filter(topic__description__exact=topic)
    ret = []
    state = Publication_status.objects.get(description="Por Aprovar")
    for publication in pubs:
        if publication.status == state:
            ret.append(publication)

    serializer = PublicationsSerializer(ret, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getSearchPublicationsFilled(request):
    author = (request.GET['author'])
    title = (request.GET['title'])
    date = (request.GET['date'])
    topic = (request.GET['topic'])
    pubs = Publications.objects.all()
    if title:
        pubs = pubs.filter(title__contains=title)
    if date:
        pubs = pubs.filter(created_on__date=date)
    if author:
        pubs = pubs.annotate(full_name=Concat('author__first_name', V(' '), 'author__last_name')). \
            filter(full_name__contains=author)
    if topic:
        pubs = pubs.filter(topic__description__exact=topic)
    ret = []
    state = Publication_status.objects.get(description="Arquivado")
    for publication in pubs:
        if publication.status == state:
            ret.append(publication)

    serializer = PublicationsSerializer(ret, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getAuthorPublicationsArquivadas(request):
    id = int(request.GET['id'])
    try:
        autor = Users.objects.get(id=id)
    except Users.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    publications = Publications.objects.all()
    ret = []
    state = Publication_status.objects.get(description="Arquivado")
    for publication in publications:
        if publication.author == autor and publication.status == state:
            ret.append(publication)
    serializer = PublicationsSerializer(ret, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getPublicationsArquivadas(request):

    publications = Publications.objects.all()
    ret = []
    state = Publication_status.objects.get(description="Arquivado")
    for publication in publications:
        if  publication.status == state:
            ret.append(publication)
    serializer = PublicationsSerializer(ret, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getAuthorFavoritePublications(request):
    id = int(request.GET['id'])
    try:
        autor = Users.objects.get(id=id)
    except Users.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    favoritos = Favorites.objects.all()
    ret = []
    for publication in favoritos:
        if publication.author == autor :
            ret.append(publication.publication)
    serializer = PublicationsSerializer(ret, many=True)
    return Response(serializer.data)








