import json
import logging

from django.http import HttpResponse
from django.utils import timezone
from django.views import View
from redis import StrictRedis

from company.models import Company
from fund.models import Fund
from fund_server import LOGGER_NAME

logger = logging.getLogger(LOGGER_NAME)

sr = StrictRedis(host="127.0.0.1", port="6379")


class FundInfoCrawl(View):

    def post(self, request):
        json_body = json.loads(request.body)
        data = json_body.get("data")

        if data:
            fund_code = data.get("fund_code")
            data["crawl_time"] = timezone.now()

            try:
                company_code = data.get("company_code")
                obj = Company.objects.get(pk=company_code)

                data["company_code"] = obj
                fund_set = Fund.objects.filter(pk=fund_code)
                if len(fund_set):  # 存在就更新
                    fund_set.update(**data)
                else:  # 不存在就创建
                    Fund.objects.create(**data)
            except Exception as e:
                logger.error(f"url: {request.path} error: {e}")
                logger.error(f"data: {data}")
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
