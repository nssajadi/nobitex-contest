import re
from django import forms
from .models import CustomUser


class CustomUserForm(forms.ModelForm):
    national_code = forms.CharField(max_length=10, min_length=10)

    def clean_full_name(self):
        cleaned_data = self.clean()
        full_name = cleaned_data.get('full_name')
        splitted_name = full_name.split(' ')
        if len(splitted_name) != 2 or re.search("^[A-Z][a-z]*(?: [A-Z][a-z]*)*$", full_name) is None:
            self.add_error('full_name', "The full name is not valid")

        return full_name

    class Meta:
        model = CustomUser
        fields = '__all__'
