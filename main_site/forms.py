from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=75)
    password = forms.CharField(widget=forms.PasswordInput())


class SignupForm(forms.Form):
    full_name = forms.CharField(label="Full Name", max_length=150)
    username = forms.CharField(label="Username", max_length=75)
    email = forms.EmailField(label="Email", max_length=254)
    password = forms.CharField(widget=forms.PasswordInput(), label="Password", max_length=150)


class SetoranHafalan(forms.Form):
    surat = forms.CharField(label="Surat", max_length=75)
    ayat = forms.IntegerField(label="Ayat")
