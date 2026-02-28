from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from main.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path('get-token/', obtain_auth_token),
]

urlpatterns += [
    path('register/', RegisterAPIView.as_view()),
    path('all_users/', UsersAPIView.as_view()),
    path('my_account/', MyAccountView.as_view()),
    path('update_account/', UpdateAccountAPIView.as_view()),
    path('change_password/', ChangePasswordAPIView.as_view()),
    path('plans/', PlansAPIView.as_view()),
]

