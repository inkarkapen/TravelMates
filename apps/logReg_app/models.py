from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
import bcrypt
import re
from django.contrib import messages
class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        if len(postData['name']) < 3:
            errors["name"] = "Name should be at least 3 characters"
        if not re.match('^[a-zA-Z ]+$', postData["name"]):
            errors['name_letters'] = "Name should have letters and/or spaces only"
        if len(postData['password']) < 8:
            errors["password"] = "Password should be at least 8 characters"
        if " " in postData['password']:
            errors['password_spaces'] = "Password shoudn't have any spaces"
        if not re.match('^[a-zA-Z0-9.+_-]+$', postData['user_name']):
            errors['user_name'] = "Username should no other characters than letters, numbers, and + - _ . "
        if postData['password'] != postData['r_password']:
            errors['password_match'] = "Passwords do not match"
        if len(self.filter(user_name = postData['user_name'])) > 0:
            errors['user_name_exist'] = "User with that username already exists"
        return errors

    def creator(self, postData):
        user = self.create(name = postData['name'], user_name = postData['user_name'], password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt()))
        return user

    def login_validator(self, postData):
        errors = {}
        users = self.filter(user_name = postData['user_name'])
        if len(users) < 1:
            errors['user_name'] = "Username doesn't exist"
        else: 
            if not bcrypt.checkpw(postData['password'].encode(), users[0].password.encode()):
                errors['password'] = "Password doesn't match"
        return errors

class User(models.Model):
    name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length = 100, default='000000' )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()