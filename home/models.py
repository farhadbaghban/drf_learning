from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.PositiveSmallIntegerField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="uquestios")
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50)
    body = models.TextField()
    crated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} -- {self.title[:50]}"


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="uanswer")
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="qanswer"
    )
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} -- {self.question.user.username}"
