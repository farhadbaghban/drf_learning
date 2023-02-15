from django.urls import path
from . import views


app_name = "home"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home_view"),
    path("question/", views.QuestionView.as_view(), name="question_view"),
    path("question/<int:pk>/", views.QuestionView.as_view(), name="question_view"),
]
