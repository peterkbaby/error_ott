from django.urls import path
from . import views

urlpatterns = [
    #auth
    path('', views.loginuser, name = 'loginuser'),
    path('logout/', views.logoutuser, name = 'logoutuser'),
    
    #home and landing
    path('landing/', views.landingpage, name = 'landingpage'),
    
    #video crud
    path('current/',views.currentvideos, name = 'currentvideos'),
    path('create/',views.createvideo, name = 'createvideo'),
    path('viewvideo/<int:video_pk>',views.viewvideo, name = 'viewvideo'),
    path('viewvideo/<int:video_pk>/delete',views.deletevideo, name = 'deletevideo'),

    #plan crud
    path('plans/',views.currentplans, name = 'currentplans'),
    path('createplan/',views.createplan, name = 'createplan'),
    path('viewplan/<int:plan_pk>',views.viewplan, name = 'viewplan'),
    path('viewplan/<int:plan_pk>/delete',views.deleteplan, name = 'deleteplan'),


    
 
    
    
    
]