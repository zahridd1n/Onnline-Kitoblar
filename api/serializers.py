from rest_framework.serializers import ModelSerializer, SerializerMethodField
from main import models


class CategorySerializer(ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'


class BooksSerializer(ModelSerializer):
    class Meta:
        model = models.Books
        fields = '__all__'


class AuthorListSerializer(ModelSerializer):
    books = BooksSerializer(many=True, read_only=True)
    audio_books = BooksSerializer(many=True, read_only=True)

    class Meta:
        model = models.Author
        fields = ['id', 'full_name', 'image', 'birthday', 'dead_day', 'books', 'audio_books', ]
        depth = 2


class AuthorDetailSerializer(ModelSerializer):
    books = BooksSerializer(many=True, read_only=True)

    class Meta:
        model = models.Author
        fields = ['id', 'full_name', 'image', 'bio', 'description', 'birthday', 'dead_day', 'books', ]


class IqtiboslarSerializer(ModelSerializer):
    class Meta:
        model = models.Iqtiboslar
        fields = '__all__'


class BooksListSerializer(ModelSerializer):
    class Meta:
        model = models.Books
        fields = ['id', 'name', 'image', 'author', 'reviews', 'reviews_count']
        depth = 2


class BookDetailSerializer(ModelSerializer):
    iqtiboslar = IqtiboslarSerializer(many=True, read_only=True)

    class Meta:
        model = models.Books
        fields = ['id', 'name', 'image', 'author', 'reviews', 'reviews_count',
                  'page', 'year', 'publisher', 'description', 'category', 'paper_book',
                  'price', 'audio_book', 'audio_book_file', 'electron_book', 'electron_book_file', 'iqtiboslar', ]
        depth = 2