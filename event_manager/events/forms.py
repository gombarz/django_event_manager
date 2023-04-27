""" 
in the forms.py we create the forms for the event app
"""
from django import forms 
from django.core.exceptions import ValidationError
from . import models 

class EventForm(forms.ModelForm):
    class Meta:
        model = models.Event
        # fields = "__all__"
        exclude = ("author",)

        widgets = {
            "date": forms.DateInput(
                format=("%Y-%m-%d %H:%M"), attrs={"type": "datetime-local"}
            )
        }
    
    def clean(self):
        """ 
        cross field validation: Validate two or more fields together
        """
        super().clean()  # creates the cleaned_data dict
        sub_title = self.cleaned_data.get("sub_title")
        name = self.cleaned_data.get("name")

        if sub_title == name:
            raise ValidationError(
                "Name and subtitle must not have the same value"
            )

        return self.cleaned_data

    
    def clean_sub_title(self) -> str:
        """ 
        Scheme: clean_<FIELDNAME>
        """
        sub_title = self.cleaned_data["sub_title"]
        illegal_chars = ("*", "#")
        if isinstance(sub_title, str) and sub_title.startswith(illegal_chars):
            raise ValidationError(
                "the Subtitle must not start with one of the illegal characters!"
            )
        return sub_title

        


class CategoryForm(forms.ModelForm):
    """a Modelform renders a form based on a model."""
    class Meta:
        model = models.Category
        fields = "__all__"  # must be a list OR __all__
        # fields = ("name", "sub_title")