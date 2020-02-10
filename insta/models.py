# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from vote.models import VoteModel

# Create your models here.
class Profile(models.Model):
    photo = models.ImageField(upload_to='images', default='profile.png')
    bio = HTMLField(blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def update_bio(cls,id, bio):
        update_profile = cls.objects.filter(id = id).update(bio = bio)
        return update_profile

    @classmethod
    def get_all_profiles(cls):
        profile = Profile.objects.all()
        return profile
    @classmethod
    def search_user(cls,user):
        return cls.objects.filter(user__username__icontains=user).all()


class Image(VoteModel,models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', default='text.png')
    caption = models.CharField(max_length=200)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    like_add = models.PositiveIntegerField(default=0)
