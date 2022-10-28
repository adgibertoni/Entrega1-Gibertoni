from django.db import models
from ckeditor.fields import RichTextField

class Report(models.Model):
    report_title = models.CharField(max_length=50)
    description = RichTextField(null=True, blank=True)
    date_added = models.DateField()

    def __str__(self):
        return f"Reporte: {self.report_title}"