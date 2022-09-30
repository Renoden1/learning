# Generated by Django 4.1.1 on 2022-09-29 11:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stock', '0003_currency_stock_description_stock_logo_stock_currency'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AccountStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('average_buy_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.account')),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.stock')),
            ],
            options={
                'unique_together': {('account', 'stock')},
            },
        ),
        migrations.CreateModel(
            name='AccountCurrency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.account')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.currency')),
            ],
            options={
                'unique_together': {('account', 'currency')},
            },
        ),
    ]
