from django.shortcuts import render, HttpResponse


def home(request):
    name = ["Hridoy", "Badhon", "Sagor", "Bijoy"]
    # contact = {"name": name}
    return render(request, "home.html", {"name": name})
