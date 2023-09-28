from typing import Any
from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView

# from tuition_App.models import Contact


def home(request):
    if request.method == "POST":
        # if request.method == "GET":
        name = ["Hridoy", "Badhon", "Sagor", "Bijoy"]
    else:
        name = ["Hridoy"]

    contact = {
        "name": name,
    }
    return render(request, "home.html", contact)


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["msg"] = "Welcome to our website"
        context["msg2"] = "Welcome to our website Again"
        return context
