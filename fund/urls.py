from django.urls import path

from fund.views import FundView

urlpatterns = [
    path('add/', FundView.as_view()),
]
