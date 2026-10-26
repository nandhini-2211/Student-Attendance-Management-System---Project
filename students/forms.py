
from django import forms
from .models import Student


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = [
            'name',
            'email',
            'age',
            'department',
            'class_name'
        ]

        widgets = {
            'class_name': forms.TextInput(attrs={
                'placeholder': 'e.g. First Year, Second Year, III BCA'
            }),
        }

    def clean_age(self):
        age = self.cleaned_data['age']

        if age < 1:
            raise forms.ValidationError(
                "Age must be at least 1."
            )

        return age
