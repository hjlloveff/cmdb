# Generated by Django 2.1 on 2019-05-14 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0016_hostinfo_shujuzhongxin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostinfo',
            name='shujuzhongxin',
            field=models.CharField(max_length=128, null=True),
        ),
    ]