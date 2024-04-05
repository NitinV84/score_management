from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .views import *

router = DefaultRouter()
router.register("applications", ApplicationCreateView)


urlpatterns = [
    
    path('',include(router.urls)),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('application/', ApplicationListCreateAPIView.as_view()),
    # path('applications/<int:pk>/', ApplicationStatusAPIView.as_view()),
    path('register/', UserRegistrationView.as_view()),
    path('profile/<int:pk>/', ProfileView.as_view()),

]