from django.shortcuts import render, HttpResponse


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
