from django.contrib.auth.models import User, Group
from rest_framework import serializers
from BB.models import  Forum, Topic, Post

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        #fields = ('url', 'name')

class ForumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Forum

class TopicSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Topic