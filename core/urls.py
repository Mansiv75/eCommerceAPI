from django.urls import path
from .views import USerRegistrationView

urlpatterns=[
    path('register/', USerRegistrationView.as_view(), name='user_register')
]