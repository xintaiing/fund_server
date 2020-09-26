# Generated by Django 3.1.1 on 2020-09-26 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fund', '0002_fund_company_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fund',
            name='fund_id',
        ),
        migrations.AddField(
            model_name='fund',
            name='crawl_time',
            field=models.DateTimeField(default=None, null=True, verbose_name='抓取时间'),
        ),
        migrations.AlterField(
            model_name='fund',
            name='fund_code',
            field=models.CharField(max_length=32, primary_key=True, serialize=False, verbose_name='基金代码'),
        ),
    ]
