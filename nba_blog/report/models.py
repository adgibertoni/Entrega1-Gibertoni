from django.db import models

class Report(models.Model):
    report_title = models.CharField(max_length=50)
    report_data = models.TextField()
    date_added = models.DateField()

    def __str__(self):
        return f"Reporte: {self.report_title}"