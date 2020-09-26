from django.db import models


# Create your models here.
class Company(models.Model):
    company_code = models.CharField(primary_key=True, verbose_name="公司编码", max_length=16)
    company_name = models.CharField(verbose_name="公司名称", default=None, null=True, max_length=128)
    establish_date = models.DateTimeField(verbose_name="公司成立时间", default=None, null=True)
    company_star = models.CharField(verbose_name="公司星级", default=None, null=True, max_length=128)
    company_money = models.CharField(verbose_name="管理资金", default=None, null=True, max_length=128)
    latest_date = models.CharField(verbose_name="资金规模最近更新时间", default=None, null=True, max_length=128)
    fund_count = models.CharField(verbose_name="基金数量", default=None, null=True, max_length=128)
    fund_manager_count = models.CharField(verbose_name="基金经理数量", default=None, null=True, max_length=128)
    crawl_time = models.DateTimeField(verbose_name="抓取时间", default=None, null=True)

    class Meta:
        db_table = "company"
        verbose_name_plural = "基金公司"
