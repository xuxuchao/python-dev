# Generated by Django 2.0.5 on 2018-08-25 02:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apiautotest', '0004_auto_20180818_1616'),
    ]

    operations = [
        migrations.CreateModel(
            name='HttpRunResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response', models.TextField(verbose_name='响应结果')),
                ('header', models.TextField(verbose_name='响应header')),
                ('statusCode', models.IntegerField(verbose_name='状态码')),
                ('assertResult', models.CharField(max_length=20, null=True, verbose_name='断言结果')),
                ('httpapi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiautotest.HttpApi', verbose_name='所属接口')),
            ],
        ),
    ]
