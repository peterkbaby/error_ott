from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.http import HttpResponse 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import VideoForm, PlanForm
from .models import Video, Subscription_Plan
from django.db import IntegrityError



def loginuser(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        user = authenticate(request, username = request.POST['username'], password = request.POST['password'])
        if user is None:
            return render(request,'login.html',{ 'error':'Username and password does not match'})
        else:
            login(request, user)
            return redirect('currentvideos')




@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('loginuser')
    else:
        return redirect('loginuser')
    
    



@login_required
def landingpage(request):
    return render(request,"landing.html")

#videocrud
@login_required
def createvideo(request):
    if request.method == "GET":
        return render(request,"create.html", {'form':VideoForm()})
    else:
        try:
            form = VideoForm(request.POST, request.FILES)
            newVideo = form.save(commit=False)
            newVideo.user = request.user
            newVideo.save()
            return redirect('currentvideos')
        except ValueError:
            return render(request, 'create.html',{'form':'VideoForm()','error':'Bad data entered'})    
@login_required
def currentvideos(request):
    videos = Video.objects.all()
    return render(request, "current.html", {'videos': videos})

@login_required
def viewvideo(request, video_pk):
    video = get_object_or_404(Video, pk = video_pk)
    if request.method == 'GET':
        form = VideoForm(instance=video)
        return render(request, 'viewvideo.html',{'video':video,'form':form})
    else:
        try:
            form = VideoForm(request.POST,request.FILES, instance=video)
            form.save()
            return redirect('currentvideos')
        except ValueError:
            return render(request, 'viewvideo.html',{'video':video, 'form':form, 'error':'Bad info'})
        
        
@login_required
def deletevideo(request, video_pk):
    video = get_object_or_404(Video, pk = video_pk)
    if request.method == 'GET':
        return render(request,'current.html')    
    else:
        try:
            
            video.delete()
            return redirect('currentvideos')
        except IntegrityError:
            return render(request, 'current.html')
        
        
#plans
@login_required
def currentplans(request):
    plans = Subscription_Plan.objects.all()
    return render(request, 'plans/currentplan.html',{'plans': plans})

def createplan(request):
    if request.method == "GET":
        return render(request,"plans/createplan.html", {'form':PlanForm()})
    else:
        try:
            form = PlanForm(request.POST)
            newPlan = form.save(commit=False)
            newPlan.user = request.user
            newPlan.save()
            return redirect('currentplans')
        except ValueError:
            return render(request, 'plans/createplan.html',{'form':'PlanForm()','error':'Bad data entered'})    

    
def viewplan(request, plan_pk):
    plan = get_object_or_404(Subscription_Plan, pk = plan_pk)
    if request.method == 'GET':
        form = PlanForm(instance=plan)
        return render(request, 'plans/viewplan.html',{'plan':plan,'form':form})
    else:
        try:
            form = PlanForm(request.POST, instance=plan)
            form.save()
            return redirect('currentplans')
        except ValueError:
            return render(request, 'plans/viewplan.html',{'plan':plan, 'form':form, 'error':'Bad info'})


def deleteplan(request, plan_pk):
    plan = get_object_or_404(Subscription_Plan, pk = plan_pk)
    if request.method == 'GET':
        return render(request,'currentplan.html')    
    else:
        try:
            
            plan.delete()
            return redirect('currentplans')
        except IntegrityError:
            return render(request, 'currentplan.html')