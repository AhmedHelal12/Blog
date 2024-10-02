from django.urls import path
from .views import CreatePostView,UpdatePostView,DeletePostView,handle_post_view,category_view,list_post_view
urlpatterns = [
    path('',list_post_view,name='list_posts'),
    path('create/post',CreatePostView.as_view(),name='create_post'),
    path('category/<int:pk>',category_view,name='category'),
    # path('search/',category_view,name='category'),
    path('update/post/<int:pk>',UpdatePostView.as_view(),name='update_post'),
    path('delete/post/<int:pk>',DeletePostView.as_view(),name='delete_post'),
    path('view/post/<int:pk>',handle_post_view,name='view_post'),
]
