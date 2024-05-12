from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from django.contrib.auth import login, logout, authenticate

from main import models
from . import serializers


@api_view(['POST'])
def sign_up(request):
    username = request.data.get('username')
    phone = request.data.get('phone')
    email = request.data.get('email')
    password = request.data.get('password')
    user = models.User.objects.create_user(username=username, phone=phone, email=email, password=password)
    return Response({'user created': 'success'})


@api_view(['POST'])
def sign_in(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return Response({'user logged in': 'success'})
    else:
        return Response({'user logged in': 'failed'})


@api_view(['POST'])
def log_out(request):
    logout(request)
    return Response({'user logged out': 'success'})


@api_view(['GET'])
@authentication_classes([BasicAuthentication, SessionAuthentication])
def authors_list(request):
    categories = models.Category.objects.all()
    categories_serializer = serializers.CategorySerializer(categories, many=True)
    authors = models.Author.objects.all()
    authors_serializer = serializers.AuthorListSerializer(authors, many=True)

    return Response({
        'categories': categories_serializer.data,
        'authors': authors_serializer.data
    })


@authentication_classes([BasicAuthentication, SessionAuthentication])
class AuthorDetailView(generics.RetrieveAPIView):
    queryset = models.Author.objects.all()
    serializer_class = serializers.AuthorDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'


@authentication_classes([BasicAuthentication, SessionAuthentication])
@api_view(['GET'])
def books_list(request):
    categories = models.Category.objects.all()
    categories_serializer = serializers.CategorySerializer(categories, many=True)
    books = models.Books.objects.all()
    books_serializer = serializers.BooksListSerializer(books, many=True)
    return Response({
        'books': books_serializer.data,
        'categories': categories_serializer.data
    })


@authentication_classes([BasicAuthentication, SessionAuthentication])
class BookDetailView(generics.RetrieveAPIView):
    queryset = models.Books.objects.all()
    serializer_class = serializers.BookDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
