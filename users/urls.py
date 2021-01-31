from django.conf.urls import url
from django.urls import path
from . import views
from rest_framework_jwt.views import verify_jwt_token


urlpatterns = [
    path("register", views.CreateUserAPIView.as_view(), name="users"),
    path("login", views.authenticate_user, name="login"),
    #path("update", views.UserRetrieveUpdateAPIView.as_view(), name="update")
    url(r'^update/$', views.UpdateUserView.as_view()),
    #url(r'^api-token-verify/', verify_jwt_token),

]
