# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Profile(models.Model):
    photo = models.ImageField(upload_to='images', default='profile.png')
    bio = HTMLField(blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
