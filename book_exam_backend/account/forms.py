from django.contrib.auth.forms import UserCreationForm

from .models import User

class SignupForm(UserCreationForm):
    class Meta:
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "firstname",
            "lastname",
            "role",
            "prefix"
        )