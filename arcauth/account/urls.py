from django.urls import path
from .views import UserLogin, index

urlpatterns = [
    path('', index, name="index"),
    path('api/login/', UserLogin.as_view(), name='login'),
]
