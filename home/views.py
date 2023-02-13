from django.shortcuts import render
from django.views import View
from django.contrib import messages


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "home/index.html")
