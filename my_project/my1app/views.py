from django.shortcuts import render
from my1app.forms import UserForm,UserProfileInfoForm

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login,logout,authenticate

# Create your views here.

def index(request):
    context_dict = {'text':'helo hola','number':2000}
    return render(request,'my1app/index.html',context_dict)
    
def relative(request):
    return render(request,'my1app/relative_url_templates.html')
    
def other(request):
    return render(request,'my1app/other.html')

def registration(request):

    registered = False
    if request.method == 'POST':

        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid and profile_form.is_valid:
            #save user attributes
            user =user_form.save()
            user.set_password(user.password)
            user.save()

            #save profile fields
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
                        
    return render(request,'my1app/registration.html',
    {'user_form':user_form,'profile_form':profile_form,'registered':registered})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("yu log indd")

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")   

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('special'))
            else:
                return HttpResponse("not actibe") 
        else:
            print("failed")
            return HttpResponse("invalid fields")
    else:
        return render(request, 'my1app/login.html')                    