from django.shortcuts import render,redirect,HttpResponse
from signup.forms import SignUpform
from django.contrib.auth import authenticate,login,logout

def signup_view(request):
        if request.method == 'POST':
            new = SignUpform(request.POST)
            if new.is_valid():
                new.save()
                return redirect('login')
        else:
            new = SignUpform()
        return render(request,'signup.html',{'form':new})
        




def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return render(request,'next.html')
    return render(request,'login.html')


def next(request):
    return render(request,'next.html')

def logout_view(request):
    logout(request)
    return render(request,'signup.html')