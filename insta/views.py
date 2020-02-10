# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .forms import ProfileForm,ImageForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Image, Profile,Comments,Likes
from vote.managers import VotableManager

# Create your views here.
votes=VotableManager()
