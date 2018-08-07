from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder": "Product Title"}))
    email = forms.EmailField()
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={
        "placeholder": "Product Description",
        "class": "new-class-name",
        "id": "my-text-area-id",
        "rows": 20,
        "cols": 120
    }
    ))
    price = forms.DecimalField(initial=199.99)

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        #if "TEST" in title:
        return title
        #raise forms.ValidationError("This is not a valid title")

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        #if not email.endswith("edu"):
            #raise forms.ValidationError("This is not valid email.")
        return email


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