from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "stock","description", "thumbnail", "category", "is_featured"]

    def clean_name(self):
        name = self.cleaned_data.get("name", "")
        return strip_tags(name)

    def clean_description(self):
        description = self.cleaned_data.get("description", "")
        return strip_tags(description)

    def clean_category(self):
        category = self.cleaned_data.get("category", "")
        return strip_tags(category)

    def clean_image_url(self):
        image_url = self.cleaned_data.get("image_url", "")
        return strip_tags(image_url)