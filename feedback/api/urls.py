from django.contrib import admin
from django.urls import path, include
from feedback.api.views import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetails.as_view()),
    path('cvs/', views.CvList.as_view()),
    path('cvs/<int:pk>/', views.CvDetails.as_view()),
    path('comments/', views.CommentList.as_view()),
    path('comments/<int:pk>/', views.CommentDetails.as_view()),
    path('likes/', views.LikeList.as_view()),
    path('likes/<int:pk>/', views.LikeDetails.as_view()),
    path('follows/', views.FollowList.as_view()),
    path('follows/<int:pk>/', views.FollowDetails.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
