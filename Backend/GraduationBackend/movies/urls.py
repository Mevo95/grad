from django.urls import path
from . import views

urlpatterns = [
    path ('user/create/',views.UserRegistration.as_view(),name='user_create'),
    path ('post/create/',views.PostCreation.as_view(),name='postCreate'),
    path ('comment/create/',views.CommentCreation.as_view(),name='commentCreate'),

    path ('user/',views.UserListView.as_view,name='userList'),
    path ('post/',views.PostListView.as_view(),name='postList'),
    path ('comment/',views.CommentListView.as_view(),name='commentList'),
    
    path ('user/<int:pk>/',views.UserDetailsView.as_view(),name='userinfo'),
    path ('post/<int:pk>/',views.postDetailview.as_view(),name='postinfo'),
    path ('comment/<int:pk>/',views.CommentDetailview.as_view(),name='commentinfo'),
    
    path ('user/<int:pk>/update',views.UserUpdateView.as_view(),name='userUpdate'),
    path ('post/<int:pk>/update',views.PostUpdateView.as_view(),name='postUpdate'),
    path ('comment/<int:pk>/update',views.CommentUpdateView.as_view(),name='commentUpdate'),
    
    
]