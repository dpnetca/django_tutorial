from django import forms

from .models import GetAnimal


class GetAnimalForm(forms.ModelForm):
    class Meta:
        model = GetAnimal
        fields = ("species", "breed", "name")


class GetNameForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=50)
    middle_name = forms.CharField(
        label="Middle Name", max_length=50, required=False
    )
    last_name = forms.CharField(label="Last Name", max_length=50)
