from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationFrom(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("email", "username")

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        fields = ("email", "username",)
