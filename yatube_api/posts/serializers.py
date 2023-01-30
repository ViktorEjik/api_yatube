from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Comment, Group, Post

User = get_user_model()


class GroupSerializers(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class PostSerializers(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)
    author = serializers.StringRelatedField()

    class Meta:
        model = Post
        fields = ('author', 'group', 'id', 'image', 'pub_date', 'text')

    def create(self, validated_data):
        if 'group' not in self.initial_data:
            post = Post.objects.create(**validated_data)
            return post
        group = validated_data.pop('group')
        post = Post.objects.create(**validated_data)
        post.group = group
        post.save()
        return post


class CommentSerializers(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('post',)
