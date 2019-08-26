from django import forms

# creating your forms here
class LoginForm(forms.Form):
    Email=forms.EmailField()
    Password=forms.PasswordInput()


