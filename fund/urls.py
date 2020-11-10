from django.urls import path

from fund.views import *

urlpatterns = [
    path('crawl/', FundInfoCrawl.as_view()),
    path('info/', FundInfoShow.as_view()),
]
