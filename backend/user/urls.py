from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    #videos
    path('videos/', views.getVideos, name='videos'),
    path('videos/<str:pk>', views.getVideo, name='getvideo'),
    
    #auth
    path('users/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    path('users/profile/', views.GetUserProfile, name="users-profile"),
    path('users/profile/update/', views.updateUserProfile, name="users-profile-update"),

    path('users/', views.GetUsers, name="users"),
    path('users/register/', views.registerUser, name="register"),
    
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)