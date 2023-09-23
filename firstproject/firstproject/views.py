from django.shortcuts import render, HttpResponse
from tuition_App.models import Contact


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


def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        phone = request.POST["phone"]
        content = request.POST["content"]
        obj = Contact(name=name, phone=phone, content=content)
        # model manager
        obj.save()
    return render(request, "contact.html")
