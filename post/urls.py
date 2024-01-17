from django.urls import path

from post.views import index, category_list, create_category_view

urlpatterns = [
    path('', index, name='index'),
    path('list/', category_list, name='category_list'),
    path('category/', create_category_view, name='create_category'),
]