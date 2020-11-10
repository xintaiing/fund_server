import json
import logging
from typing import Dict

from django.http import HttpResponse
from django.utils import timezone
from django.views import View

from company.models import Company
from fund_server import LOGGER_NAME

logger = logging.getLogger(LOGGER_NAME)


def _check_data_format(data: Dict):
    if data.get("company_code"):
        return data
    return None


class CompanyInfoCrawl(View):

    def post(self, request):
        json_body = json.loads(request.body)
        data = json_body.get("data")
        company_code = data.get("company_code")
        data["crawl_time"] = timezone.now()

        data = _check_data_format(data)
        if data:
            company_set = Company.objects.filter(pk=company_code)
            try:
                if len(company_set):
                    company_set.update(**data)
                else:
                    Company.objects.create(**data)
            except Exception as e:
                logger.error(f"url: {request.path} error: {e}")
                logger.error(f"data: {data}")
            return HttpResponse("数据成功添加！")
        return HttpResponse("数据格式有误！")
