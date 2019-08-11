from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.utils.datastructures import MultiValueDictKeyError
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        try:
            password = request.POST['password']
        except MultiValueDictKeyError:
            password = False
        user = auth.authenticate(request, username=username, password=password)
        
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request , 'login.html',{'error':'username or password is incorrect.'})
    else:
        return render(request , 'login.html')


def signup(request):    
    if request.method == 'POST':
        if request.POST.get('password1') == request.POST.get('password2'):
            user = User.objects.create_user(username = request.POST.get('username') ,password = request.POST.get('password1'))
            auth.login(request, user)
            return redirect('home')
    return render(request, 'signup.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'login.html')