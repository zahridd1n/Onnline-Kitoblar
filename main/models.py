from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Avg


class User(AbstractUser):
    status = models.IntegerField(
        choices=(
            (1, 'yosh kitobxon'),
            (2, 'kumush kitobxon'),
            (3, 'oltin kitobxon'),
        ), null=True, blank=True, default=1
    )
    bio = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='media/user/', blank=True, null=True)

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Author(models.Model):
    full_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/author/')
    bio = models.TextField()
    description = models.TextField()
    birthday = models.DateTimeField()
    dead_day = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.full_name

    @property
    def books(self):
        return Books.objects.filter(author=self)

    @property
    def audio_books(self):
        return Books.objects.filter(author=self, audio_book=True)


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)


class Books(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/books/')
    page = models.IntegerField()
    year = models.DateField()
    description = models.TextField()
    publisher = models.ForeignKey(Publisher, null=True, on_delete=models.SET_NULL, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    paper_book = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    audio_book = models.BooleanField(default=False)
    audio_book_file = models.FileField(upload_to='media/audio_book/', blank=True, null=True)
    electron_book = models.BooleanField(default=False)
    electron_book_file = models.FileField(upload_to='media/electron_book/', blank=True, null=True)

    def __str__(self):
        return self.name

    @property
    def reviews(self):
        data = Review.objects.filter(book=self)
        count = data.count()
        if count == 0:
            return 0
        else:
            total_mark = sum(review.mark for review in data)
            return total_mark / count

    @property
    def iqtiboslar(self):
        return Iqtiboslar.objects.filter(book=self)

    @property
    def reviews_count(self):
        return Review.objects.filter(book=self).count()


class Review(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mark = models.FloatField()
    text = models.TextField(blank=True, null=True)


class Iqtiboslar(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    body = models.TextField()
