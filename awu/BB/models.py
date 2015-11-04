# -*- coding: UTF-8 -*-
from django.db import models
from django.contrib import admin


class Category(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(default='')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(blank=True, null=True)


class Forum(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120)
    category = models.ForeignKey(Category)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    num_topics = models.IntegerField(default=0)
    num_posts = models.IntegerField(default=0)
    description = models.TextField(default='')
    ordering = models.PositiveIntegerField(default=1)
    