from django.db.models import fields
from .models import Firms
from django.forms import ModelForm, TextInput


class FirmsForm(ModelForm):
    class Meta:
        model = Firms
        fields = ['firm_name']