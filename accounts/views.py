from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        # value in form get from POST (like http)
        # if user click on submit make a form with filled value
        # save in database
        form = UserCreationForm(request.POST)
        # if values are valid
        if form.is_valid():
            # get users details
            user = form.save()
            login(request, user)
            # login
            # redirect to another page after sign up
            return redirect('articles:list')
    else:
            # if method is not 'POST' means it is 'GET'
            # Create new form for user
            # After click 'submit' first time the return to this method see
            # this time method is 'POST' so if execute
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form' : form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # login user
            user = form.get_user()
            login(request, user)
            # find values that post to server
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:    
                return redirect('articles:list')
    else:
        # method 'GET'
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form' : form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('articles:list')