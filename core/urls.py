from django.urls import path
from .views import UserRegistrationView
from .views import CustomTokenObtainPairView

urlpatterns=[
    path('register/', UserRegistrationView.as_view(), name='user_register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
]