from django.shortcuts import render
from .models import Contact
from .forms import ContactForm

# Create your views here.


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        # name = request.POST["name"]
        if form.is_valid():
            name = form.cleaned_data["name"]
            phone = form.cleaned_data["phone"]
            content = form.cleaned_data["content"]
            obj = Contact(name=name, phone=phone, content=content)
            # model manager
            obj.save()
    else:
        form = ContactForm()
    return render(request, "contact.html", {"form": form})
