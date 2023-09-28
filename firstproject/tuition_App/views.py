from django.shortcuts import render
from .models import Contact, Post, Subject
from .forms import ContactForm, PostForm
from django.http.response import HttpResponse
from django.views import View


# class base views
class ContactView(View):
    form_class = ContactForm
    template_nmae = "contact.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_nmae, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Success")
        return render(request, self.template_nmae, {"form": form})


# Create your views here.


# def contact(request):
#     if request.method == "POST":
#         form = ContactForm(request.POST)
#         # name = request.POST["name"]
#         if form.is_valid():
#             form.save()
#     else:
#         form = ContactForm()
#     return render(request, "contact.html", {"form": form})


def postview(request):
    post = Post.objects.all()
    return render(request, "tuition/postview.html", {"post": post})


def subview(request):
    sub = Subject.objects.get(name="English")
    post = sub.subject_set.all()
    return render(request, "tuition/subjectview.html", {"sub": sub, "post": post})


def postcreate(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()

            sub = form.cleaned_data["subject"]
            for i in sub:
                obj.subject.add(i)
                obj.save()
            class_in = form.cleaned_data["class_in"]
            for i in class_in:
                obj.class_in.add(i)
                obj.save()
            return HttpResponse("Success")

    else:
        form = PostForm()
    return render(request, "tuition/postcreate.html", {"form": form})
