from app.models import Groups, Users, Publication_status, Publication_topics, Publications, Comments, Favorites
from rest_framework import serializers





class GroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = ('id','description')


class PublicationStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication_status
        fields = ('id','description')


class PublicationTopicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication_topics
        fields = ('id','description')


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id','username','first_name', 'last_name', 'group')


class PublicationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publications
        fields = ('id','title','content', 'created_on', 'author','status','topic')


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('id','comment','author', 'publication')


class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        fields = ('id','author','publication')


class FavoritesSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        fields = ('author','publication')




