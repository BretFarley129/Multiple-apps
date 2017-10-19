# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect


def index(request):
    response = "placeholder to later display the list of all users"
    return HttpResponse(response)

def register(request):
    response = "placeholder to create a new user record!"
    return HttpResponse(response)

def login(request):
    response = "placeholder for users to login"
    return HttpResponse(response)



