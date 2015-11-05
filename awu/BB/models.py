# -*- coding: UTF-8 -*-
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(default='')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(blank=True, null=True)


class Forum(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120)
    category = models.ForeignKey(Category)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(blank=True, null=True)
    num_topics = models.IntegerField(default=0)
    num_posts = models.IntegerField(default=0)
    description = models.TextField(default='')
    ordering = models.PositiveIntegerField(default=1)
    def __unicode__(self):
        return self.title

    def num_posts(self):
        return sum([t.num_posts() for t in self.topic_set.all()])
		
class Topic(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(max_length=10000, blank=True, null=True)
    forum = models.ForeignKey(Forum)
    created = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    closed = models.BooleanField(blank=True, default=False)

    def num_posts(self):
        return self.post_set.count()

    def num_replies(self):
        return max(0, self.post_set.count() - 1)

    def last_post(self):
        if self.post_set.count():
            return self.post_set.order_by("created")[0]

    def __unicode__(self):
        return unicode(self.creator) + " - " + self.title

class Post(models.Model):
    title = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    topic = models.ForeignKey(Topic)
    body = models.TextField(max_length=10000)
    user_ip = models.GenericIPAddressField(blank=True, null=True)

    def __unicode__(self):
        return u"%s - %s - %s" % (self.creator, self.topic, self.title)

    def short(self):
        return u"%s - %s\n%s" % (self.creator, self.title, self.created.strftime("%b %d, %I:%M %p"))

    short.allow_tags = True