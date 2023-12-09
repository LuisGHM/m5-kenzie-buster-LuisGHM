from django.urls import path
from .views import UserView, LoginJWTView, UserByIdView

urlpatterns = [
    path("users/", UserView.as_view()),
    path("users/<int:user_id>/", UserByIdView.as_view()),
    path("users/login/", LoginJWTView.as_view()),
]