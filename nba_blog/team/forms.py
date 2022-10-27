from django import forms


class TeamForm(forms.Form):
    city = forms.CharField(
        label="Ciudad:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "team-city",
                "placeholder": "Ingrese la ciudad",
                "required": "True",
            }
        ),
    )
    name = forms.CharField(
        label="Nombre:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "team-city",
                "placeholder": "Ingrese el nombre",
                "required": "True",
            }
        ),
    )
    owner = forms.CharField(
        label="Dueño actual:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "team-city",
                "placeholder": "Ingrese el nombre del dueño",
                "required": "True",
            }
        ),
    )
    found_in = forms.DateField(
        label="Fecha de fundación:",
        required=False,
        widget=forms.DateInput(
            attrs={
                "class": "team-city",
                "placeholder": "yyyy-mm-dd",
                "required": "True",
            }
        ),
    )
    
