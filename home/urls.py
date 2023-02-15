from django.urls import path
from . import views


app_name = "home"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home_view"),
    path("questions/", views.QuestionListView.as_view(), name="question_List_view"),
    path(
        "question/create/",
        views.QuestionCreateView.as_view(),
        name="question_Create_view",
    ),
    path(
        "question/update/<int:pk>/",
        views.QuestionUpdateView.as_view(),
        name="question_Update_view",
    ),
    path(
        "question/delete/<int:pk>/",
        views.QuestionDeleteView.as_view(),
        name="question_Delete_view",
    ),
]
