import json
import logging
from typing import Dict

from django.http import HttpResponse
from django.utils import timezone
from django.views import View
from redis import StrictRedis

from company.models import Company
from fund.models import Fund
from fund_server import LOGGER_NAME

logger = logging.getLogger(LOGGER_NAME)

sr = StrictRedis(host="127.0.0.1", port="6379")


def _check_data_format(data: Dict):
    if data.get("company_code") and data.get("fund_code"):
        return data
    return None


class FundInfoCrawl(View):

    def post(self, request):
        """
        添加爬取的基金信息
        """
        json_body = json.loads(request.body)
        data = _check_data_format(json_body.get("data"))

        if data:
            # 生成爬取数据时间
            data["crawl_time"] = timezone.now()

            fund_set = Fund.objects.filter(pk=data.get("fund_code"))
            if len(fund_set):  # 存在就更新
                fund_set.update(**data)
            else:  # 不存在就创建
                data["company_code"] = Company.objects.get(pk=data.get("company_code"))
                Fund.objects.create(**data)
            return HttpResponse("数据成功添加！")
        return HttpResponse("数据格式有误！")


class FundInfoShow(View):

    def get(self, request):
        """
        显示所有基金
        """
        print(request.path)
        cache = sr.lpop(request.path)
        if not cache:
            company_set = Fund.objects.all()[:100]
            result = [str(item) for item in company_set.values()]
            sr.lpush(request.path, json.dumps(result))
            print("==")
        else:
            print("--")
            result = json.loads(cache)
        return HttpResponse(content_type="application/json", content=json.dumps(result))
