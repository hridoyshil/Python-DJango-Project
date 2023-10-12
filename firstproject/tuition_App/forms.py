from django import forms
from django.forms import widgets
from .models import Contact, Post


class ContactForm(forms.ModelForm):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter Your name"}
        ),
        label="Your name",
    )

    class Meta:
        model = Contact
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["name"].label = "My Name"
        self.fields["name"].initial = "My Name"
        self.fields["phone"].initial = "+8801"
        self.fields["content"].initial = "My problem is"

    def clean_name(self):
        value = self.cleaned_data.get("name")
        num_of_w = value.split(" ")
        if len(num_of_w) > 3:
            self.add_error("name", "Name can have maximun of 3 words")
        else:
            return value


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


from .models import PostFile


class FileModelForm(forms.ModelForm):
    class Meta:
        model = PostFile
        fields = ["image"]
