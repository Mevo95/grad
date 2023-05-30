from rest_framework import serializers
from .models import User, Post, Comment

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, write_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user    
      

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'date_posted', 'author')
        
class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    post = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = ('id', 'content', 'date_posted', 'author', 'post')