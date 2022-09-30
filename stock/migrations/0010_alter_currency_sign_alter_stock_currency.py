# Generated by Django 4.1.1 on 2022-09-29 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0009_alter_stock_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='sign',
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name='stock',
            name='currency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock.currency'),
        ),
    ]
