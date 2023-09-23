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


def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        phone = request.POST["phone"]
        content = request.POST["content"]
        print(name)
        print(phone)
        print(content)
    return render(request, "contact.html")
