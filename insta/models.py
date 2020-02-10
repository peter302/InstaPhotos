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



class Likes(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save_likes(self):
        self.save()

    def delete_like(self):
        self.delete()

    def count_likes(self):
        likes = self.likes.count()
        return likes

class Comments(models.Model):
    comment = models.CharField(max_length = 50, blank=True)
    posted = models.DateTimeField(auto_now_add=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    # @classmethod
    # def get_comments_by_images(self):
    #     comments = Image.objects.filter(image_id = id )
    #     return comments

    @classmethod
    def get_comments(cls,id):
        comments = cls.objects.filter(image__id=id)
        return comments


    def __str__(self):
        return self.comment
