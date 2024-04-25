from django.urls import path
from customer.views import *

urlpatterns = [
    path("",CustomerSignup.as_view()),
    path("login/",CustomerLogin.as_view(),name="log-in")
]