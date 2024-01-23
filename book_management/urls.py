from django.urls import path
from book_management import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('book_list/', views.book_list, name='book_list'),
    path('add_book_list/', views.add_book_list, name='add_book_list'),
    path('author_list/', views.author_list, name='author_list'),
    path('add_author_list/', views.add_author_list, name='add_author_list'),
    path('edit_author_list/<id>/', views.edit_author_list, name='edit_author_list'),
    path('update_author_list/<id>/', views.update_author_list, name='update_author_list'),
    path('delete_author_list/<id>/', views.delete_author_list, name='delete_author_list'),
    path('edit_book_list/<id>/', views.edit_book_list, name='edit_book_list'),
    path('update_book_list/<id>/', views.update_book_list, name='update_book_list'),
    path('delete_book_list/<id>/', views.delete_book_list, name='delete_book_list'),
    path('author_ser/', views.author_ser),
    path('singleauthor/<id>/', views.SingleAuthor),
    path('book_ser/', views.book_ser),
    path('singlebook/<id>/', views.SingleBook),
]