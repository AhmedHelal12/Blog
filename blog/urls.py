from django.urls import path
from .views import CreatePostView,ListPostView,UpdatePostView,DeletePostView,handle_post_view
urlpatterns = [
    path('',ListPostView.as_view(),name='list_posts'),
    path('create/post',CreatePostView.as_view(),name='create_post'),
    path('update/post/<int:pk>',UpdatePostView.as_view(),name='update_post'),
    path('delete/post/<int:pk>',DeletePostView.as_view(),name='delete_post'),
    path('view/post/<int:pk>',handle_post_view,name='view_post'),
]
