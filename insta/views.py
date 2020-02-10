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

@login_required(login_url='/accounts/login/')
def index(request):
    current_user = request.user
    posts = Image.get_all_images()
    comments = Comments.objects.all()
    profile = Profile.get_all_profiles()


    return render(request, 'istagram/index.html', locals())

def add_image(request):
        current_user = request.user
        if request.method == 'POST':
                form = ImageForm(request.POST, request.FILES)
                if form.is_valid():
                        add=form.save(commit=False)
                        add.user = current_user
                        add.save()
                return redirect('index')
        else:
                form = ImageForm()
                return render(request,'istagram/image.html', {"form":form})    
