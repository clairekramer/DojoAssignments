from __future__ import unicode_literals
from django.db import models
import bcrypt
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

class UserManager(models.Model):
    def validate_reg(self, postData):
        errors = {}
        for field, value in postData.iteritems():
            if len(value) < 1:
                errors[field] = 'All Fields are Required'
        if 'email' not in errors and not re.match(EMAIL_REGEX, postData['email']):
            errors['email'] = 'Invalid Email'
        if 'email' not in errors and len(self.filter(email=postData['email'])) > 0:
            errors['email'] = 'Email already in use'
        if 'password' not in errors and len(postData['password']) < 8:
            errors['password'] = 'Password must be at least 8 Characters'
        if 'password' not in errors and postData['password'] != postData['confirm']:
            errors['password'] = 'Passwords do not match'
        if len(errors) > 0:
            return errors
        hashed = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
        new_user = self.create(
            name=postData['name'],
            email=postData['email'],
            password=hashed
        )
        return new_user

    def validate_login(self, postData):
        errors = {}
        if len(self.filter(email = postData['email'])) > 0:
            user = self.filter(email = postData['email'])[0]
            if not bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
                errors['password'] = 'Incorrect Password'
        else:
            errors['email'] = 'Incorrect Email'
        if errors:
            return errors
        return user

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    objects = UserManager()
    def __repr__(self):
        return 'User: {}'.format(self.name)

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
