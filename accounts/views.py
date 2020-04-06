from django.shortcuts import render, redirect
from django.contrib import messages, auth 
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            
            # check username
            if User.objects.filter(username=username).exists():
                messages.error(request, "Provided username already registered.")
                return redirect('register')
            else:

                # check the email
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Provided email account already registered.")
                    return redirect('register')
                else:
                    # Looks good
                    user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, 
                    email=email, password=password)
                    user.save()
                    messages.success(request, 'You have successfully registered. Please login.')
                    return redirect('login')
        else:
            messages.error(request, "Password do not match.")
            return redirect('register')

        
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "You have successfully logged in.")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid credentials.")
            return redirect('login')


    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, "You have successfully logged out.")
        return redirect('index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')

