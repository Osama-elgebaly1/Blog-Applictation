from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('post/<int:pk>',views.post,name='post'),
    path('tags/<slug:tag>',views.get_tags,name='tags'),
    path('add_comment',views.add_comment,name='add_comment'),
    path('delete_comment/',views.delete_comment,name='delete_comment'),
    path('last_post/',views.last_post,name='last_post'),
    path('contact/',views.contact,name='contact'),
    path('create_blog/',views.create_blog,name='create_blog'),
    path('edit_post/<int:pk>',views.edit_blog,name='edit_blog'),
    path('delete_blog/<int:pk>',views.delete_blog,name='delete_blog'),
  
    
]
