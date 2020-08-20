from django.urls import path, include
from rest_framework import renderers
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('books', views.BookViewSet, basename='books-api')

urlpatterns = [
    path('', include(router.urls)),
]