from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from app.models import Author, Groups, Users, Publication_status, Publication_topics, Publications, Comments, Favorites
from app.serializers import AuthorSerializer, GroupsSerializer, UsersSerializer, PublicationStatusSerializer, \
    PublicationTopicsSerializer, PublicationsSerializer, CommentsSerializer, FavoritesSerializer


# Create your views here.

@api_view(['GET'])
def get_author(request):
    id = int(request.GET['id'])
    try:
        author = Author.objects.get(id=id)
    except Author.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = AuthorSerializer(author)
    return Response(serializer.data)


@api_view(['GET'])
def get_authors(request):
    authors= Author.objects.all()
    if 'num' in request.GET:
        num=int(request.GET['num'])
        authors=authors[:num]

    serializer = AuthorSerializer(authors,many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_author(request):
    serializer = AuthorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_author(request):
    id = request.data['id']
    try:
        author=Author.objects.get(id=id)
    except Author.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer=AuthorSerializer(author,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def del_author(request,id):
    try:
        author=Author.objects.get(id=id)
    except Author.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    author.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# Métodos do Groups


@api_view(['GET'])
def get_group(request):
    groups = Groups.objects.all()

    #PROVAVELMENTE VAI SER PRECISO DIZER QUEM PEDIU PARA SABER QUE GRUPOS LHE MANDAR

    serializer = GroupsSerializer(groups, many=True)
    return Response(serializer.data)


# Métodos do User
@api_view(['PUT'])
def update_User(request):
    id = request.data['id']
    try:
        user=Users.objects.get(id=id)
    except Users.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer=UsersSerializer(user,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_users(request):
    users= Users.objects.all()
    # Devo precisar de saber quem me pediu para saber quantos lhe posso mostrar mas depois ponho isto
    # que agora ainda estou na fase de tentar meter tudo o que é preciso

    serializer = UsersSerializer(users,many=True)
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
#Nao vai ter create nem delete so vai ter gets


@api_view(['GET'])
def pub_status_getALl(request):

    ret = Publication_status.objects.all()
    serializer = PublicationStatusSerializer(ret, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def pub_status_getOne(request):
    #Acho que é melhor fazer o get Pela descrição do que pelo id
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
    #Penso que faça mais sentido fazer o get pela descrição do que pelo id
    id = int(request.GET['id'])
    try:
        ret = Publication_topics.objects.get(id=id)
    except Publication_topics.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = PublicationTopicsSerializer(ret)
    return Response(serializer.data)


@api_view(['GET'])
def get_pub_topics(request):
    ret= Publication_topics.objects.all()
    serializer = PublicationTopicsSerializer(ret,many=True)
    return Response(serializer.data)


@api_view(['POST'])
def get_pub_topics_create(request):
    serializer = PublicationTopicsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def get_pub_topics_update(request):
    # Não sei se vai ser pelo id se pela descrição, vou deixar pelo id e mais tarde troca-se se for preciso
    id = request.data['id']
    try:
        ret=Publication_topics.objects.get(id=id)
    except Publication_topics.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer=PublicationTopicsSerializer(ret,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def get_pub_topics_delete(request,id):
    try:
        ret=Publication_topics.objects.get(id=id)
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
    ret= Publications.objects.all()
    serializer = PublicationsSerializer(ret,many=True)
    return Response(serializer.data)


@api_view(['POST'])
def pubcrate(request):
    serializer = PublicationsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def pubupd(request):
    id = request.data['id']
    try:
        ret=Publications.objects.get(id=id)
    except Publications.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer=PublicationsSerializer(ret,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def pubdel(request,id):
    try:
        ret=Publications.objects.get(id=id)
    except Publications.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    ret.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

##COMMENTS
    #NOS NO OUTRO PROJETO NÃO TINHAMOS O UPDATE DE UM COMENTÁRIO não sei se querem colocar ou não, se quiserem
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
    ret= Comments.objects.all()
    serializer = CommentsSerializer(ret,many=True)
    return Response(serializer.data)


@api_view(['POST'])
def commentcre(request):
    serializer = CommentsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)




@api_view(['DELETE'])
def commentdel(request,id):
    try:
        ret=Comments.objects.get(id=id)
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
    ret= Favorites.objects.all()
    serializer = FavoritesSerializer(ret,many=True)
    return Response(serializer.data)


@api_view(['POST'])
def favcre(request):
    serializer = FavoritesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)




@api_view(['DELETE'])
def favdel(request,id):
    try:
        ret=Favorites.objects.get(id=id)
    except Favorites.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    ret.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

