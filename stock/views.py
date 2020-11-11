import json
from datetime import datetime
from typing import Dict

from django.http import HttpResponse
from django.utils import timezone
from django.views import View

from fund.models import Fund
from stock.models import Stock, FundStockShip


def _check_data_format(data: Dict):
    if data.get("fund_code") and data.get("stock_code"):
        return data
    return None


def str_to_datetime(value):
    """
    字符串时间 转换成 datetime
    :param value:
    :return:
    """
    if value is None or value == "":
        return ""
    return datetime.strptime(value, '%Y-%m-%d')


class StockInfoCrawl(View):

    def post(self, request):
        json_body = json.loads(request.body)
        data = _check_data_format(json_body.get("data"))
        deadline_date = json_body.get("deadline_date")
        if data:
            data["crawl_time"] = timezone.now()
            proportion = data.pop("proportion")
            fund_obj = Fund.objects.get(pk=data.pop("fund_code"))
            stock_set = Stock.objects.filter(pk=data.get("stock_code"))
            if len(stock_set):  # 当前股票已经存在
                stock_obj = stock_set.first()
            else:  # 不存在，添加创建当前股票
                stock_obj = Stock.objects.create(**data)

            FundStockShip.objects.create(fund=fund_obj,
                                         stock=stock_obj,
                                         proportion=proportion,
                                         deadline_date=str_to_datetime(deadline_date),
                                         crawl_time=data.get("crawl_time"))
            return HttpResponse("数据成功添加！")
        return HttpResponse("数据格式有误！")
