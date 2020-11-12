import json
from datetime import datetime
from typing import Dict

from django.http import HttpResponse
from django.utils import timezone
from django.views import View

from fund.models import Fund
from stock.models import Stock, FundStockShip, FundFundShip


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
        flag = json_body.get("flag")
        if data:
            crawl_time = timezone.now()
            proportion = data.pop("proportion")
            fund_obj = Fund.objects.get(pk=data.pop("fund_code"))
            if flag == "stock":  # 股票持仓
                stock_set = Stock.objects.filter(pk=data.get("stock_code"))
                if len(stock_set):  # 当前股票已经存在
                    stock_obj = stock_set.first()
                else:  # 不存在，添加创建当前股票
                    data["crawl_time"] = crawl_time
                    stock_obj = Stock.objects.create(**data)

                fund_stock_set = FundStockShip.objects.filter(stock=stock_obj.stock_code,
                                                              fund=fund_obj.fund_code)
                if len(fund_stock_set):
                    fund_stock = fund_stock_set.first()
                    fund_stock.proportion = proportion
                    fund_stock.deadline_date = deadline_date
                    fund_stock.crawl_time = crawl_time
                    fund_stock.save()
                else:
                    FundStockShip.objects.create(fund=fund_obj,
                                                 stock=stock_obj,
                                                 proportion=proportion,
                                                 deadline_date=str_to_datetime(deadline_date),
                                                 crawl_time=crawl_time)

            else:  # 基金持仓
                fund_fund_set = FundFundShip.objects.filter(fund=fund_obj.fund_code,
                                                            related_fund_code=data.get("related_fund_code"))
                if len(fund_fund_set):
                    fund_fund = fund_fund_set.first()
                    fund_fund.proportion = proportion
                    fund_fund.fluctuation = data.get("fluctuation")
                    fund_fund.deadline_date = deadline_date
                    fund_fund.crawl_time = crawl_time
                    fund_fund.save()
                else:
                    FundFundShip.objects.create(fund=fund_obj,
                                                related_fund_code=data.get("related_fund_code"),
                                                related_fund_name=data.get("related_fund_name"),
                                                proportion=proportion,
                                                fluctuation=data.get("fluctuation"),
                                                deadline_date=deadline_date,
                                                crawl_time=crawl_time)
            return HttpResponse("数据成功添加！")
        return HttpResponse("数据格式有误！")
