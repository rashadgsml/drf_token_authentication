from django.urls import path
from .views import PostList, PostDetail

app_name = 'core'

urlpatterns = [
    path('', PostList.as_view(), name = 'post-list'),
    path('post-detail/<str:pk>', PostDetail.as_view(), name = 'post-detail'),

]
