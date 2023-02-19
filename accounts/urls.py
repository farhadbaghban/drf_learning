from django.urls import path
from rest_framework import routers

# from rest_framework.authtoken import views as auth_token
from . import views


"""
    using api token generator
"""

app_name = "accounts"

urlpatterns = [
    # path("register", views.UserRegisterView.as_view(), name="register"),
    # path("api-token-auth/", auth_token.obtain_auth_token),
]

router = routers.SimpleRouter()
router.register("user", views.UserViewSet, basename="user")
urlpatterns += router.urls
