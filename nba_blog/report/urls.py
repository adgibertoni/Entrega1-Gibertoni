from django.urls import path

from report import views

app_name = "report"
urlpatterns = [
    #path("report", views.reports, name="report-list"),
    #path("report/add", views.report_create, name="report-add"),
    path("reports/", views.ReportListView.as_view(), name="report-list"),
    path("report/add/", views.ReportCreateView.as_view(), name="report-add"),
    path("report/<int:pk>/detail/", views.ReportDetailView.as_view(), name="report-detail"),
    path("report/<int:pk>/update/", views.ReportUpdateView.as_view(), name="report-update"),
    path("report/<int:pk>/delete/", views.ReportDeleteView.as_view(), name="report-delete"),

]