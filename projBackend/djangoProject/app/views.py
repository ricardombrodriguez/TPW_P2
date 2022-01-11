from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from app.models import Author
from app.serializers import AuthorSerializer


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
