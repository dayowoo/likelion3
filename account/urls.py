from django.urls import path
from .import views
urlpatterns = [
    path('sign-in/', views.sign_in, name="sign_in"),
    path('sign-out/', views.sign_out, name="sign_out"),
    path("sign-up/", views.sign_up,name="sign_up"),
]