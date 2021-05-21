from django.urls import path
from books import views

urlpatterns = [
    path('home/', views.viewHome),
    path('insert/', views.insertBook),
    path('view/', views.viewBook),
    path('save/', views.insert),
    path('edit/', views.editBook),
    path('update/', views.update),
    path('delete/', views.deleteBook),
    path('search/', views.searchForm),
    path('searching/', views.search),
    path('userlogin/', views.userLogin),
    path('userlogout/', views.userLogout),
]
