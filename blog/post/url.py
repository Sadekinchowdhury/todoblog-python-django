from django.urls import path
from .views import Homepage, Details, CreatePost, Delete, updatePost


urlpatterns = [
    path('', Homepage.as_view(), name='home'),
    path('<int:pk>/', Details.as_view(), name='details'),
    path('newpost/', CreatePost.as_view(), name='newpost'),
    path('delete/<int:pk>/', Delete.as_view(), name='delete'),
    path('update/<int:pk>/', updatePost.as_view(), name='update')
]
