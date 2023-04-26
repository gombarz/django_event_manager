""" 
in the forms.py we create the forms for the event app
"""
from django import forms 
from . import models 

class CategoryForm(forms.ModelForm):
    """a Modelform renders a form based on a model."""
    class Meta:
        model = models.Category
        fields = "__all__"  # must be a list OR __all__
        # fields = ("name", "sub_title")