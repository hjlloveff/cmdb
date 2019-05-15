# Generated by Django 2.1 on 2019-05-15 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0018_hostinfo_xiangmu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hostinfo',
            name='inip',
        ),
        migrations.RemoveField(
            model_name='hostinfo',
            name='name',
        ),
        migrations.RemoveField(
            model_name='hostinfo',
            name='outip',
        ),
        migrations.RemoveField(
            model_name='hostinfo',
            name='shujuzhongxin',
        ),
        migrations.RemoveField(
            model_name='hostinfo',
            name='xiangmu',
        ),
        migrations.AddField(
            model_name='hostinfo',
            name='belong_business',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='hostinfo',
            name='cpu_type',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='hostinfo',
            name='data_center',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='hostinfo',
            name='disk_total',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='hostinfo',
            name='display_name',
            field=models.CharField(max_length=128, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='hostinfo',
            name='gpu_type',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='hostinfo',
            name='hold_type',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='hostinfo',
            name='mem_total',
            field=models.IntegerField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='hostinfo',
            name='num_cpus',
            field=models.IntegerField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='hostinfo',
            name='num_gpus',
            field=models.IntegerField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='hostinfo',
            name='os_type',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='hostinfo',
            name='private_ip',
            field=models.CharField(max_length=128, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='hostinfo',
            name='public_ip',
            field=models.CharField(max_length=128, null=True, unique=True),
        ),
    ]