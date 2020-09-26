from django.db import models

from company.models import Company


class Fund(models.Model):
    fund_code = models.CharField(primary_key=True, max_length=32, verbose_name="基金代码")
    fund_name = models.CharField(max_length=128, verbose_name="基金名称", default=None, null=True)
    fund_type = models.CharField(max_length=128, verbose_name="基金类型", default=None, null=True)
    fund_date = models.CharField(max_length=128, verbose_name="日期", default=None, null=True)
    unit_net_worth = models.CharField(max_length=128, verbose_name="单位净值", default=None, null=True)
    total_net_worth = models.CharField(max_length=128, verbose_name="累计净值", default=None, null=True)
    growth_rate = models.CharField(max_length=128, verbose_name="日增长率", default=None, null=True)
    six_month = models.CharField(max_length=128, verbose_name="近六个月", default=None, null=True)
    one_year = models.CharField(max_length=128, verbose_name="近一年", default=None, null=True)
    fund_money = models.CharField(max_length=128, verbose_name="基金规模", default=None, null=True)
    fund_manager = models.CharField(max_length=128, verbose_name="基金经理", default=None, null=True)
    buy_status = models.CharField(max_length=128, verbose_name="申购状态", default=None, null=True)
    handling_fee = models.CharField(max_length=128, verbose_name="手续费", default=None, null=True)
    company_code = models.ForeignKey(Company, on_delete=models.CASCADE, default=None, null=True)
    crawl_time = models.DateTimeField(verbose_name="抓取时间", default=None, null=True)

    class Meta:
        db_table = "fund"
        verbose_name_plural = "基金信息"
