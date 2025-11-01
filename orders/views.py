from django import forms
from django.shortcuts import redirect, render

from .models import Combo, MenuItem, Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            "full_name",
            "email",
            "menu_item",
            "quantity",
            "extras",
            "delivery_method",
            "address",
        ]
        widgets = {
            "full_name": forms.TextInput(),
            "email": forms.EmailInput(),
            "menu_item": forms.Select(),
            "quantity": forms.NumberInput(),
            "extras": forms.CheckboxSelectMultiple(),
            "delivery_method": forms.RadioSelect(),
            "address": forms.Textarea(),
        }


def home(request):
    if request.method == "POST":
        form = OrderForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("home")

    else:
        form = OrderForm()

    context = {
        "menu_items": MenuItem.objects.all(),
        "combos": Combo.objects.all(),
        "form": form,
    }

    return render(request, "index.html", context)
