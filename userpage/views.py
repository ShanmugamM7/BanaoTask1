
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, LoginForm
from django.contrib import messages
def index(request):
    return render(request, 'index.html')

def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)  
        if form.is_valid():
            # password = form.cleaned_data.get('password')
            # confirm_password = form.cleaned_data.get('confirm_password')
            # if password != confirm_password:
            #     messages.error(request, 'Passwords do not match. Please enter matching passwords.')
            #     return render(request, 'signup.html', {'form': form})
            user = form.save()
            login(request, user)
            if user.user_type == 'P':
                return redirect('login')  # Replace 'patient_dashboard' with the actual URL name
            elif user.user_type == 'D':
                return redirect('login')  # Replace 'doctor_dashboard' with the actual URL name
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                if user.user_type == 'P':
                    return redirect('patient_page')  # Replace 'patient_dashboard' with the actual URL name
                elif user.user_type == 'D':
                    return redirect('doctor_page')  # Replace 'doctor_dashboard' with the actual URL name
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

def patient_page(request):
    patient_data = request.user  # This should give you the logged-in patient's data
    context = {
        'patient_data': patient_data,
    }
    return render(request, 'patient_page.html', context)

def doctor_page(request):
    doctor_data = request.user  # This should give you the logged-in doctor's data
    context = {
        'doctor_data': doctor_data,
    }
    return render(request, 'doctor_page.html', context)
