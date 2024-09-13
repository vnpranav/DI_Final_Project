from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from store.forms import CustomUserForm


def register(request):
   form = CustomUserForm()
   if request.method == 'POST':
      form = CustomUserForm(request.POST)
      if form.is_valid():
         form.save()
         messages.success(request, "Registered successfully, Login to continue")
         return redirect('/login')
   context = {'form' : form}
   return render(request, 'store/auth/register.html', context)

def loginpage(request):
   if request.user.is_authenticated:
      messages.warning(request, 'You are already logged in')
      return redirect('/index')
   else:
      if request.method == 'POST':
         username = request.POST.get('username')
         password = request.POST.get('password')
         user = authenticate(request, username=username, password=password)

         if user is not None:
            login(request, user)
            messages.success(request , "Logged in successfully")
            return redirect('/index')
         else:
            messages.error(request, "Invalid username or password")
            return redirect('/login')
         
   return render(request, 'store/auth/login.html')

def logoutpage(request):
   if request.user.is_authenticated:
      logout(request)
      messages.success(request, "Logoged out successfully")
      return redirect('/login')
   else:
      messages.warning(request, "You are not logged in")
      return redirect('/login')