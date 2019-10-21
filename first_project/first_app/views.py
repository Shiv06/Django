from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Webpage,AccessRecord
from . import forms
from itertools import chain

# Extra import for login and logout
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required



def index(request):
    return render(request,'first_app/index.html')

def register(request):

    registered=False

    if request.method=='POST':
        user_form=forms.UserForm(data=request.POST)
        profile_form=forms.UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user
            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']
            profile.save()
            registered=True

        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form=forms.UserForm()
        profile_form=forms.UserProfileInfoForm()

    return render(request,'first_app/registration.html',context={'user_form':user_form,
                                                                 'profile_form':profile_form,
                                                                 'registered': registered})
@login_required
def special_welcome(request):
    return HttpResponse("You have logged in Successfully")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def user_login(request):
    if request.method=='POST':
        username=request.POST.get('user_name')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)


        if user:
            if user.is_active:
                login(request, user)
                print(reverse('index'))
                return HttpResponseRedirect(reverse('index'))
            else:
                HttpResponse("YOUR ACCCOUNT IS NOT ACTIVE!")
        else:
            print('Someone Tried to login, but failed!')
            print('Username: {username} and password: {password} is used'.format(username,password))
            return HttpResponse("Invalid login.Either username or password is incorrect!")

    else:
        return render(request,'first_app/login.html')









def webdetails(request):
    acc_record= AccessRecord.objects.order_by('date')
    webpages=Webpage.objects.all()
    for acc in acc_record:
        acc_record.wepages=Webpage.objects.filter(name=acc.webpageName)


    # for web in webpages:
    #     print(web.date)

    context_dic={'AccessRecords':acc_record,'webpages':webpages}
    return render(request,'first_app/webdetails.html',context=context_dic)






# Create your views here.
