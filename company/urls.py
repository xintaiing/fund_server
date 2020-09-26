from django.urls import path

from company.views import CompanyView

urlpatterns = [
    path('add/', CompanyView.as_view()),
]
