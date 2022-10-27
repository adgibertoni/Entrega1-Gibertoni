from django import forms


class ReportForm(forms.Form):
    report_title = forms.CharField(
        label="Título del reporte:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "player-name",
                "placeholder": "Ingrese el título",
                "required": "True",
            }
        ),
    )
    report_data = forms.CharField(
        label="Descripción:",
        required=False,
        widget=forms.TextInput(
            attrs={
                
                "placeholder": "Ingrese la información correspondiente al reporte",
                "required": "True",
            }
        ),
    )
    date_added = forms.DateField(
        label="Fecha:",
        required=False,
        widget=forms.DateInput(
            attrs={
                "class": "player-name",
                "placeholder": "yyyy-mm-dd",
                "required": "True",
            }
        ),
    )
