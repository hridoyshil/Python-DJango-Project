from django import forms
from django.forms import widgets
from .models import Contact, Post


class ContactForm(forms.ModelForm):
    # name = (
    #     forms.CharField(
    #         max_length=100,
    #         widget=forms.TextInput(
    #             attrs={"class": "form-control", "placeholder": "Enter Your Name"}
    #         ),
    #     ),
    # )

    class Meta:
        model = Contact
        fields = "__all__"

        # Form Design--MOdel Form
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Your Name"}
            ),
            "phone": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter Your Phone"}
            ),
            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Say something",
                    "rows": 5,
                }
            ),
        }
        labels = {
            "name": "Your Name",
            "phone": "Your Phone Number",
            "content": "Your Words",
        }
        help_texts = {
            "name": "Your Name",
            "phone": "Your Phone Number",
            "content": "Your Words",
        }


# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         exclude = ["user", "id", "created_at", "slug"]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ["user", "id", "created_at", "slug", "likes", "views"]
        widgets = {
            "class_in": forms.CheckboxSelectMultiple(
                attrs={
                    "multiple": True,
                }
            ),
            "subject": forms.CheckboxSelectMultiple(
                attrs={
                    "multiple": True,
                }
            ),
        }
