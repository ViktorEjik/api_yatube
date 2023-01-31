from django.contrib.auth import get_user_model
from posts.models import Comment, Group, Post
from rest_framework import serializers

User = get_user_model()


class GroupSerializers(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class PostSerializers(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Post
        fields = ('author', 'group', 'id', 'image', 'pub_date', 'text')


class CommentSerializers(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('post',)
