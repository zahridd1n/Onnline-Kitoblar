from django.urls import path
from . import views

urlpatterns = [
    path('sign-up/', views.sign_up),
    path('sign-in/', views.sign_in),
    path('log-out/', views.log_out),

    path('author/list/', views.authors_list),
    path('author/detail/<int:id>/', views.AuthorDetailView.as_view()),

    path('book/list/', views.books_list),
    path('book/detail/<int:id>/', views.BookDetailView.as_view()),
    # path('contact/', views.contact, name='contact'),
]


