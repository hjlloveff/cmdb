# Generated by Django 2.1 on 2019-05-13 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0013_auto_20190513_0436'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hostinfo',
            name='hostaccsess_id',
        ),
        migrations.RemoveField(
            model_name='hostinfo',
            name='hostitem_id',
        ),
        migrations.AddField(
            model_name='hostinfo',
            name='hostaccsess_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='asset.hostaccessinfo'),
        ),
        migrations.AddField(
            model_name='hostinfo',
            name='hostitem_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='asset.iteminfo'),
        ),
    ]
