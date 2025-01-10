from django.urls import include, path
# from rest_framework import routers
# from app.views import UserViewSet
from app import views

# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('login', views.LoginView.as_view()),
    path('user/detail', views.UserDetailView.as_view()),
]
