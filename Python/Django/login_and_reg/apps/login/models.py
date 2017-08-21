from __future__ import unicode_literals
from django.db import models
import bcrypt
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

class UserManager(models.Manager):
    def validate(self, postData):
        errors = {}
        for field, value in postData.iteritems():
            if len(value) < 1:
                errors[field] = 'All Fields are Required'
            if field == 'first_name' or field == 'last_name':
                if not field in errors and len(value) < 2:
                    errors[field] = '{} field must be at least 2 characters'.format(field.replace('_', ''))
        if 'email' not in errors and not re.match(EMAIL_REGEX, postData['email']):
            errors['email'] = 'Invalid Email'
        else:
            if len(self.filter(email=postData['email'])) > 0:
                errors['email'] = 'Email already in use'
        if 'password' not in errors and len(postData['password']) < 8:
            errors['password'] = 'Password must be at least 8 Characters'
        if 'password' not in errors and postData['password'] != postData['confirm']:
            errors['password'] = 'Passwords do not match'
        if len(errors) > 0:
            return errors

        hashed = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
        new_user = self.create(
            first_name=postData['first_name'],
            last_name=postData['last_name'],
            email=postData['email'],
            password=hashed
        )
        return new_user

    def validate_login(self, postData):
        errors = {}
        if len(self.filter(email = postData['email'])) > 0:
            user = self.filter(email=postData['email'])[0]
            if not bcrypt.checkpw(postData['password'].encode(), user.password.encode()):
                errors['password'] = 'Incorrect Password'
        else:
            errors['email'] = 'Incorrect Email'
        if errors:
            return errors
        return user

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    objects = UserManager()
    def __repr__(self):
        return 'User: {} {}'.format(self.first_name, self.last_name)
