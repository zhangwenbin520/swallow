# Generated by Django 2.1 on 2019-04-20 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cabinet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='机柜号')),
            ],
            options={
                'verbose_name': '机柜',
                'verbose_name_plural': '机柜',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Idc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='机房名称', max_length=32, unique=True, verbose_name='机房名称')),
                ('address', models.CharField(blank=True, help_text='机房地址', max_length=128, null=True, verbose_name='机房地址')),
                ('phone', models.CharField(blank=True, help_text='机房电话', max_length=16, null=True, verbose_name='机房电话')),
                ('remark', models.TextField(blank=True, help_text='备注', max_length=255, null=True, verbose_name='备注')),
                ('create_date', models.DateTimeField(auto_now_add=True, help_text='创建时间', max_length=32, null=True, verbose_name='创建时间')),
                ('update_date', models.DateTimeField(auto_now=True, help_text='更新时间', max_length=32, null=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': 'IDC机房',
                'verbose_name_plural': 'IDC机房',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='cabinet',
            name='idc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='idc_cab', to='idc.Idc', verbose_name='所处机房'),
        ),
    ]