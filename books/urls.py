from django.urls import path
from . import views

urlpatterns = [
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
    path('books/<int:book_id>/review/', views.submit_review, name='submit_review'),
]