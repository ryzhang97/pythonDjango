from django.urls import include, path
from wx.views import LoginView
from wx.views import AccessTokenView

urlpatterns = [
    path('login', LoginView.as_view(), name="login"),
    path('getAccess', AccessTokenView.as_view()),
]
