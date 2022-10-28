from datetime import datetime
from django.contrib import messages
#from django.core.paginator import Paginator
#from django.http import HttpResponse
from django.shortcuts import render
#from django.template import loader

from django.core.exceptions import ValidationError
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from report.forms import ReportForm
from report.models import Report


class ReportListView(ListView):
    model = Report
    paginate_by = 3
    template_name = "report/report_list.html"	# no hace falta ponerlo porq utilicé la forma de la convención -->

class ReportDetailView(DetailView):
    model = Report
    fields = ["report_title", "description", "date_added"]


class ReportCreateView(CreateView):
    model = Report
    success_url = reverse_lazy("report:report-list")

    form_class = ReportForm
    # fields = ["report_title", "description", "date_added"]

    def form_valid(self, form):
        """Filter to avoid duplicate reports"""
        data = form.cleaned_data
        actual_objects = Report.objects.filter(
            report_title=data["report_title"]
        ).count()
        if actual_objects:
            messages.error(
                self.request,
                f"El reporte {data['report_title']} ya fue creado",
            )
            form.add_error("report_title", ValidationError("Acción no válida"))
            return super().form_invalid(form)
        else:
            messages.success(
                self.request,
                f"Reporte: {data['report_title']} creado exitosamente!",
            )
            return super().form_valid(form)


class ReportUpdateView(UpdateView):
    model = Report
    fields = ["report_title", "description", "date_added"]

    def get_success_url(self):
        report_id = self.kwargs["pk"]
        return reverse_lazy("report:report-detail", kwargs={"pk": report_id})


class ReportDeleteView(DeleteView):
    model = Report
    success_url = reverse_lazy("report:report-list")
