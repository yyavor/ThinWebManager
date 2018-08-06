from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]


class RawProductForm(forms.Form):
    title = forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder": "Product Title"}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={
        "placeholder": "Product Description",
        "class": "new-class-name",
        "id": "my-text-area-id",
        "rows": 20,
        "cols": 120
    }
                                                                        ))
    price = forms.DecimalField(initial=199.99)