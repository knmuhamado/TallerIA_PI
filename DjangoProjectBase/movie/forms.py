from django import forms

class PromptForm(forms.Form):
    prompt = forms.CharField(
        label="",  # quitamos el label para que no repita
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ingrese el tipo de película que desea buscar (prompt)"
            }
        )
    )
