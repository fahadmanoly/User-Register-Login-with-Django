from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import HttpResponseRedirect
from django.views.decorators.cache import never_cache


# Login section
@never_cache
def user_login(request):
    if 'username' in request.session:
        return redirect('profile')
    if request.method == "POST":
        fm = AuthenticationForm(request=request, data = request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname,password=upass)
            if user is not None:
                request.session['username'] = uname
                return redirect('profile')
            else:
                print('invalid')
                

    else:
        fm = AuthenticationForm()

    return render(request, 'blog/userlogin.html', {'form':fm})

def user_logout(request):
    if 'username' in request.session:
        del request.session['username']
    return redirect('profile')
    
@never_cache
def user_profile(request):
    if 'username' in request.session:
        return render(request, 'blog/profile.html')
    else:
        return redirect('login')
    






# Sign up section.
def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()

    else:
        fm = SignUpForm() 

    return render(request, 'blog/sign_up.html', {'form': fm})



