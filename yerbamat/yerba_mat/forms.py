from django import forms

from yerba_mat.models import Category, Product, Client


class LoginForm(forms.Form):
    username = forms.CharField(label="Login", max_length=128)
    password = forms.CharField(label="Hasło", max_length=128, widget=forms.PasswordInput)


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class ProductForm(forms.Form):
    name = forms.CharField(label="Nazwa", max_length=128)
    description = forms.CharField(
        label="Opis",
        max_length=1024,
        widget=forms.Textarea(attrs={'width': "100%", 'cols': "80", 'rows': "20"}),
    )
    amount = forms.IntegerField()
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    picture = forms.ImageField()


class ProductForm2(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class ClientCreateForm(forms.Form):
    username = forms.CharField(label="Login", max_length=128)
    email = forms.CharField(label="E-mail", max_length=128)
    password = forms.CharField(label="Hasło", max_length=128, widget=forms.PasswordInput)
    name = forms.CharField(label="Imię", max_length=128)
    lastname = forms.CharField(label="Nazwisko", max_length=128)
    street = forms.CharField(label="Ulica", max_length=128)
    post = forms.CharField(label="Kod pocztowy", max_length=128)
    city = forms.CharField(label="Miasto", max_length=128)
    phone = forms.IntegerField(label="Telefon")