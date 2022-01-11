from app.models import Author
from rest_framework import serializers


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model= Author
        fields= ('id','name','email')