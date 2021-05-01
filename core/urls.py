from django.urls import path
from .views import PostList, PostDetail, UserList, UserDetail

app_name = 'core'

urlpatterns = [
    path('', PostList.as_view(), name = 'post-list'),
    path('post-detail/<str:pk>', PostDetail.as_view(), name = 'post-detail'),
    path('users/', UserList.as_view(), name = 'user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name = 'user-detail'),
]
