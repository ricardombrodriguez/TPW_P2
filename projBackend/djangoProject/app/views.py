from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from app.models import Author, Groups,Users
from app.serializers import AuthorSerializer, GroupsSerializer,UsersSerializer


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

##Publication Status
