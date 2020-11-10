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
        """
        添加爬取的公司信息
        """
        json_body = json.loads(request.body)
        data = _check_data_format(json_body.get("data"))

        if data:
            # 生成爬取数据时间
            data["crawl_time"] = timezone.now()

            company_set = Company.objects.filter(pk=data.get("company_code"))
            if len(company_set):
                company_set.update(**data)
            else:
                Company.objects.create(**data)
            return HttpResponse("数据成功添加！")
        return HttpResponse("数据格式有误！")
