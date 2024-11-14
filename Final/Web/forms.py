from django import forms
from .models import CustomUser, QuoteRequest

class CustomUserCreationForm(forms.ModelForm):
    confirmation = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = CustomUser
        fields = ['email', 'password']

    def clean_confirmation(self):
        password = self.cleaned_data.get("password")
        confirmation = self.cleaned_data.get("confirmation")
        if password != confirmation:
            raise forms.ValidationError("Passwords do not match.")
        return confirmation

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"]) 
        if commit:
            user.save()
        return user
class QuoteRequestForm(forms.ModelForm):
    class Meta:
        model = QuoteRequest
        fields = ['name', 'phone', 'project_type', 'location', 'details', 'budget']
        widgets = {
            'details': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Provide details about the project'}),
            'budget': forms.NumberInput(attrs={'placeholder': 'Enter your estimated budget'}),
        }
