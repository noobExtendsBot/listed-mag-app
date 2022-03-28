from rest_framework import serializers
from blog.models import Post, Categories, Comment


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title', 'author', 'post_cat', 'post_img', 'content', 'created_at', 'updated_at')
        model = Post


class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Categories


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Comment

