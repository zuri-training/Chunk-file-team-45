import string
from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

allowed_characters = set(
    string.ascii_letters +
    string.digits +
    string.punctuation
)
User = get_user_model()


class UserCreateForm(forms.Form):
    username = forms.CharField(label="Username", max_length=200, required=True)
    email = forms.EmailField(label="Email address", required=True)
    password = forms.CharField(
        widget=forms.PasswordInput, label='Password', required=True)
    confirm_password = forms.CharField(
        widget=forms.PasswordInput, label='Confirmed Password', required=True)

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

    def clean_confirm_password(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise ValidationError("Password did not match")

        if (len(password) < 8):
            raise ValidationError("password is too short")

        if not any(pass_char.isdigit() for pass_char in password):
            raise ValidationError("password must have at least one number")

        if not any(pass_char.isupper() for pass_char in password):
            raise ValidationError(
                "password must have at least one uppercase letter")

        if not any(pass_char.islower() for pass_char in password):
            raise ValidationError(
                "password must have at least one lowercase letter")

        return confirm_password

    def clean_username(self):
        username = self.cleaned_data.get("username")
        q = User.objects.filter(username__iexact=username)
        if q.exists():
            raise ValidationError("This Username is already taken")
        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        q = User.objects.filter(email__iexact=email)
        if q.exists():
            raise ValidationError("The email is already taken")
        return email


class UserLoginForm(forms.Form):

    username = forms.CharField(max_length=50)
    password = forms.CharField(
        widget=forms.PasswordInput,
        label='Password'
    )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username)
        # The iexact makes the query responed to case insensitive

        if not qs.exists():
            # exists method return a bool if or not if the query exist in the DB.
            raise forms.ValidationError(
                "Username is invalid."
            )

        return username
