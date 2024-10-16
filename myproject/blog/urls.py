from django.urls import path
from .views import home, detail, category,authorList

app_name = 'blog'
urlpatterns = [
    path('', home, name='home'),
    path('page/<int:page>', home, name='home'),
    path('article/<slug:slug>', detail, name='detail'),
    path('category/<slug:slug>', category, name='category'),
    path('category/<slug:slug>/page/<int:page>', category, name='category'),
    path('author/<slug:username>', authorList, name='author'),
    path('author/<slug:username>/page/<int:page>', authorList, name='author'),

]