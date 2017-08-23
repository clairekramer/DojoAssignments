from __future__ import unicode_literals
from django.db import models
from ..belt.models import User

class Author(models.Model):
    name = models.CharField(max_length=255)
    def __repr__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name='books')
    def __repr__(self):
        return 'Book: {} by {}'.format(self.title, self.author)

class ReviewManager(models.Manager):
    def create_review(self, postData, user_id):
        author = None
        if len(postData['new_author']) < 1:
            author = Author.objects.get(id=int(postData['author']))
        else:
            author = Author.objects.create(name=postData['new_author'])
        book = None
        if not Book.objects.filter(title=postData['title']):
            book = Book.objects.create(
                title=postData['title'],
                author = author
            )
        else:
            book = Book.objects.get(title=postData['title'])
        self.create(
            comment = postData['comment'],
            rating = postData['rating'],
            book = book,
            reviewer = User.objects.get(id=user_id)
        )

    def recent(self):
        return (self.all().order_by('-created_at')[:3], self.all().order_by('-created_at')[3:])



class Review(models.Model):
    comment = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    reviewer = models.ForeignKey(User, related_name='reviews')
    book = models.ForeignKey(Book, related_name='reviews')
    objects = ReviewManager()
    def __repr__(self):
        return 'Reviewed Book: {}'.format(self.book.title)
