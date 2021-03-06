from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

def twitterprofile(request, username):
    user = get_object_or_404(User, username=username)

    context = {
        'user' : user
    }

    return render(request, 'twitterprofile/twitterprofile.html', context)
