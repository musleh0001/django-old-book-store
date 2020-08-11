from django.urls import path
from . import views


urlpatterns = [
    path('', views.BookList.as_view(), name='book_list'),
    path('detail/<int:pk>/', views.BookDetail.as_view(), name='book_detail'),
    path('new/', views.bookCreate, name='book_new'),
    path('edit/<int:pk>/', views.BookUpdate.as_view(), name='book_update'),
    path('delete/<int:pk>/', views.BookDelete.as_view(), name='book_delete'),
    path('my_posts/', views.UserPostList.as_view(), name='my_posts'),
]