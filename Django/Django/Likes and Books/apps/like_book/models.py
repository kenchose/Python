# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    first_name=models.CharField(max_length=100)
    last_name = models.CharField(max_length = 100)
    email = models.EmailField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return "<User object: {} {}>".format(self.first_name, self.last_name)

class Book(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=100)
    uploaded_by = models.ForeignKey(User, related_name="uploader")
    liked_by = models.ManyToManyField(User, related_name = "likes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self):
        return "<Book object: {}>".format(self.name)


