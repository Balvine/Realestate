
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import UserProfile,Post,Company,Comment
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm,ostForm,CommentForm
from rest_framework.response import Response
from rest_framework.views import APIView



# Create your views here.
@login_required
def index(request):
    current_user = request.user
    # try:
    #     profile = UserProfile.objects.get(user = current_user)
    # except:
    #     return redirect('edit_profile',username = current_user.username)
