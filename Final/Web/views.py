from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CustomUser, QuoteRequest
from .forms import CustomUserCreationForm, QuoteRequestForm 
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

# Home view
def index(request):
    return render(request, 'Final/index.html')

# Pools view
def pools(request):
    return render(request, 'Final/pools.html')

@login_required
def quote(request):
    if request.method == "POST":
        form = QuoteRequestForm(request.POST)
        if form.is_valid():
            quote_request = form.save(commit=False)

            # Set the user field to the current logged-in user
            quote_request.user = request.user

            quote_request.email = request.user.email 

            quote_request.save()

            # Provide feedback to the user
            messages.success(request, "Your quote request has been submitted successfully!")
            return redirect('quote_request') 

        else:
            messages.error(request, "There was an error with your request. Please try again.")
    else:
        form = QuoteRequestForm()

    return render(request, 'Final/quote.html', {'form': form})

@login_required
def quote_request_view(request):
  
    quote_requests = QuoteRequest.objects.filter(user__email=request.user.email)

    if request.method == 'POST':
    
        quote_id = request.POST.get('quote_id')
        
        quote_request = get_object_or_404(QuoteRequest, id=quote_id, user__email=request.user.email)

        form = QuoteRequestForm(request.POST, instance=quote_request)

        if form.is_valid():
            form.save()  
            messages.success(request, "Your quote has been updated successfully!")
            return redirect('quote_request') 
        else:
            messages.error(request, "There was an error updating your quote. Please try again.")

    return render(request, 'Final/submitted.html', {'quote_requests': quote_requests})

def construction(request):
    return render(request, 'Final/construction.html')

def submit_form(request):
    return

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from .models import CustomUser

# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            # Save the new user
            form.save()
            messages.success(request, "Account created successfully! Please log in.")
            return redirect('login')  
        else:
            messages.error(request, "There was an error in your registration. Please try again.")
            return render(request, 'Final/register.html', {'form': form})

    else:
        form = CustomUserCreationForm()

    return render(request, 'Final/register.html', {'form': form})


# Login view
def login_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        # Try to find the user by email
        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            user = None

        if user and user.check_password(password): 
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user) 
            return redirect("index") 
        else:
            messages.error(request, "Invalid email or password") 
            return redirect("login") 

    return render(request, "Final/login.html")

def logout_view(request):
    logout(request)
    return redirect('index')
