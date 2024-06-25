from django.urls import include, path
from rest_framework import routers
from app.views import UserViewSet
from app.views import CustomView

router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('custom/', CustomView.as_view()),
]
