# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Dojo(models.Model):
    name=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    desc=models.CharField(max_length=255, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __repr__(self):
        return "<Dojo object: {} at {} in {}".format(self.name, self.city, self.state)

class Ninja(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    dojo=models.ForeignKey(Dojo, related_name="ninjas")  
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __repr__(self):
        return "<Ninja object: {} {}".format(self.first_name, self.last_name)