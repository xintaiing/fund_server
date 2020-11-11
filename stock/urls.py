from django.urls import path

from stock.views import *

urlpatterns = [
    path('crawl/', StockInfoCrawl.as_view()),
]
