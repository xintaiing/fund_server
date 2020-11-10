from django.urls import path

from company.views import CompanyInfoCrawl

urlpatterns = [
    path('crawl/', CompanyInfoCrawl.as_view()),
]
