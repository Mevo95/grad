from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import User, Comment, Post
from .serializers import UserSerializer, CommentSerializer, PostSerializer
from rest_framework import generics

##user
class UserRegistration(generics.CreateAPIView):
 #   def createUser(self, request):
  #      serializer = UserSerializer(data=request.data)
   #     if serializer.is_valid():
    #        user = serializer.save()
     #   return Response({'user_id': user.id, 'message': 'User created successfully'})
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()
     
        
class UserDetailsView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def perform_update(self, serializer):
        serializer.save()    

##posts    
    
class PostCreation(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    def createPost(self,serializer):
        serializer.save
        
class postDetailview(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer   

class PostUpdateView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    def perform_update(self, serializer):
        serializer.save()


##comments
class CommentCreation(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    def createComment(self,serializer):
        serializer.save

class CommentDetailview(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentListView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentUpdateView(generics.UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    def perform_update(self, serializer):
        serializer.save()            


@login_required
def create_post(request):
    if request.method == 'POST':
        # Get the form data from the request
        content = request.POST['content']
        title = request.POST['title']
         
        Post = Post.objects.create(
            content=content,
            title=title,
            author_id=request.user.id
        )
    
    return render(request, 'create_post.html')            






