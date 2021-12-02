from django.forms import ModelForm

from .models import Cart, Item

# class CompanyForm(ModelForm):


#     class Meta:
#         model = Company
#         fields = "__all__"


class ItemForm(ModelForm):

    class Meta:
        model = Item
        fields = [
            "name",
            "images",
            "sizes",
            "details",
            "rating",
            "price",
            "discount",
        ]

class ItemToCartForm(ModelForm):

    class Meta:
        model = Cart
        fields = [
            "quantity",
            "size",
        ]
