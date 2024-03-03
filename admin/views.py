from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum, Count, F, Case, When
from django.http import JsonResponse
from django.contrib import messages 
from datetime import date
from django.db import transaction, models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required

# Tommorrow.
# add variables that calculate both individual ongoing and upcoming projects budget
# add a variable that calculates all upcoming projects budget
# show closest upcoming project in dashboard
# Continue enhancing the dashboard style

def index(request):
   return render(request, 'login.html')
