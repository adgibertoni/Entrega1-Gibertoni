from django.urls import path

from report import views

app_name = "report"
urlpatterns = [
    path("report", views.reports, name="report-list"),
    path("report/add", views.create_report, name="report-add"),
]