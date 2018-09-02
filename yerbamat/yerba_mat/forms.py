from django import forms

from yerba_mat.models import Category, Product


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