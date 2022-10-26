from django import forms


class PlayerForm(forms.Form):
    name = forms.CharField(
        label="Nombre:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "player-name",
                "placeholder": "Ingrese el nombre",
                "required": "True",
            }
        ),
    )
    last_name = forms.CharField(
        label="Apellido:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "player-name",
                "placeholder": "Ingrese el apellido",
                "required": "True",
            }
        ),
    )
    country = forms.CharField(
        label="País:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "player-name",
                "placeholder": "Ingrese el país que representa",
                "required": "True",
            }
        ),
    )
    number = forms.IntegerField(
        label="Número:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "player-number",
                "placeholder": "Ingrese el número de camiseta",
                "required": "True",
            }
        ),
    )
    points = forms.FloatField(
        label="Puntos por juego:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "player-number",
                "placeholder": "Ingrese los puntos de promedio",
                "required": "True",
            }
        ),
    )
