# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
import string
import random

# Create your views here.
def index(request):
    #set the count in session
    if 'count' not in request.session:
        request.session['count'] = 0
    return render(request, 'gen_app/index.html')

#when submit button is clicked
def random_word(request):
    if request.method == "POST":
        word = generate_word()          #generate random word
        request.session['word'] = word  #set word in session
        request.session['count'] += 1   #increment count in session
        return redirect('/')
    else:
        return redirect('/')

#helper function: returns random string of length 6
def generate_word(size=8, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))




