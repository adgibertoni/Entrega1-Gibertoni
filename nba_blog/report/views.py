from datetime import datetime
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from report.forms import ReportForm
from report.models import Report

def get_reports(request):
    reports = Report.objects.all()
    paginator = Paginator(reports, 2)
    page_number = request.GET.get("page")
    return paginator.get_page(page_number)
    #return reports

def create_report(request):
    if request.method == "POST":
        report_form = ReportForm(request.POST)
        if report_form.is_valid():
            data = report_form.cleaned_data
            actual_objects = Report.objects.filter(
                report_title=data["report_title"]
            ).count()
            print("actual_objects", actual_objects)
            if actual_objects:
                messages.error(
                    request,
                    f"El reporte {data['report_title']} ya existe",
                )
            else:
                report = Report(
                    report_title=data["report_title"],
                    report_data=data["report_data"], 
                    date_added=data["date_added"],
                    )
                report.save()
                messages.success(
                    request,
                    f"El reporte {data['report_title']} ha sido creado exitosamente!",
                )

            return render(
                request=request,
                context={"reports": get_reports(request)},
                template_name="report/report_list.html",
            )

    report_form = ReportForm(request.POST)
    context_dict = {"form": report_form}
    return render(
        request=request,
        context=context_dict,
        template_name="report/report_form.html",
    )


def reports(request):
    #reports = Report.objects.all()
    #context_dict = {"reports": reports}
    return render(
        request=request,
        context={"reports": get_reports(request)}, #context_dict,
        template_name="report/report_list.html",
    )