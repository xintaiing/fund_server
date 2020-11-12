from django.db import models

from fund.models import Fund


class Stock(models.Model):
    stock_code = models.CharField(primary_key=True, max_length=32, verbose_name="股票代码")
    stock_name = models.CharField(max_length=128, verbose_name="股票名称", default=None, null=True)
    exchange_code = models.CharField(max_length=128, verbose_name="交易所", default=None, null=True)
    fluctuation = models.CharField(max_length=128, verbose_name="涨跌幅", default=None, null=True)
    fund_stock_ship = models.ManyToManyField(Fund, through='FundStockShip')
    crawl_time = models.DateTimeField(verbose_name="抓取时间", default=None, null=True)

    class Meta:
        db_table = "stock"
        verbose_name_plural = "股票信息"


class FundStockShip(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    fund = models.ForeignKey(Fund, on_delete=models.CASCADE)
    proportion = models.CharField(max_length=128, verbose_name="持仓占比", default=None, null=True)
    deadline_date = models.DateTimeField(verbose_name="持仓截止日期", default=None, null=True)
    crawl_time = models.DateTimeField(verbose_name="抓取时间", default=None, null=True)

    class Meta:
        db_table = "fund_stock"
        verbose_name_plural = "股票持仓"


class FundFundShip(models.Model):
    fund = models.ForeignKey(Fund, on_delete=models.CASCADE)
    related_fund_code = models.CharField(max_length=128, verbose_name="关联基金代码", default=None, null=True)
    related_fund_name = models.CharField(max_length=128, verbose_name="关联基金名称", default=None, null=True)
    proportion = models.CharField(max_length=128, verbose_name="持仓占比", default=None, null=True)
    fluctuation = models.CharField(max_length=128, verbose_name="涨跌幅", default=None, null=True)
    deadline_date = models.DateTimeField(verbose_name="持仓截止日期", default=None, null=True)
    crawl_time = models.DateTimeField(verbose_name="抓取时间", default=None, null=True)

    class Meta:
        db_table = "fund_fund"
        verbose_name_plural = "基金信息"
