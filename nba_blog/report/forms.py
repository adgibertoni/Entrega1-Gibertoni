from ckeditor.widgets import CKEditorWidget
from django import forms

from report.models import Report


class ReportForm(forms.ModelForm):
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
    description = forms.CharField(
        label="Descripción:",
        required=False,
        widget=CKEditorWidget(
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

    class Meta:
        model = Report
        fields = ["report_title", "description", "date_added"]