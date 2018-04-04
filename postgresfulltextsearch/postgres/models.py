# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.search import SearchVectorField


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()
    lang = models.CharField(max_length=100, default='english')

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField(auto_now_add=True)
    mod_date = models.DateField(auto_now=True)
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField(default=0)
    n_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=5)
    search_vector = SearchVectorField(null=True)

    def __str__(self):
        return self.headline