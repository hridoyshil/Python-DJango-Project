from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from .models import Contact, Post, Subject
from .forms import ContactForm, PostForm
from django.http.response import HttpResponse
from django.views import View
from django.views.generic import FormView, CreateView, ListView, DetailView
from django.urls import reverse_lazy


# Form View, Class Based View-Generic View // CBV(Class Based View)
class ContactView(FormView):
    form_class = ContactForm
    template_name = "contact.html"

    # success_url='/'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy("homeview")


# # class base views
# class ContactView(View):
#     form_class = ContactForm
#     template_name = "contact.html"

#     def get(self, request, *args, **kwargs):
#         form = self.form_class()
#         return render(request, self.template_nmae, {"form": form})

#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse("Success")
#         return render(request, self.template_nmae, {"form": form})


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


class PostDetailView(DetailView):
    model = Post
    template_name = "tuition/postdetail.html"


def postview(request):
    post = Post.objects.all()
    return render(request, "tuition/postview.html", {"post": post})


class PostListView(ListView):
    template_name = "tuition/postlist.html"
    queryset = Post.objects.filter(user=1)
    # model = Post
    context_object_name = "posts"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["posts"] = context.get("object_list")
        context["msg"] = "This is post list"
        return context


def subview(request):
    sub = Subject.objects.get(name="English")
    post = sub.subject_set.all()
    return render(request, "tuition/subjectview.html", {"sub": sub, "post": post})


class PostCreareView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "tuition/postcreate.html"
    # success_url = "/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        id = self.object.id
        return reverse_lazy("tuition_App:subjects")


# def postcreate(request):
#     if request.method == "POST":
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             obj = form.save(commit=False)
#             obj.user = request.user
#             obj.save()

#             sub = form.cleaned_data["subject"]
#             for i in sub:
#                 obj.subject.add(i)
#                 obj.save()
#             class_in = form.cleaned_data["class_in"]
#             for i in class_in:
#                 obj.class_in.add(i)
#                 obj.save()
#             return HttpResponse("Success")

#     else:
#         form = PostForm()
#     return render(request, "tuition/postcreate.html", {"form": form})
