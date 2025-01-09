from django.urls import include, path
from app import views

urlpatterns = [
    path('custom', views.CustomView.as_view()),
    path('test', views.TestView.as_view()),
    path('login',views.LoginView.as_view()),
]
