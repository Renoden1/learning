# Generated by Django 4.1.1 on 2022-09-29 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0005_alter_stock_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='sign',
            field=models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior'), ('GR', 'Graduate')], default='FR', max_length=2),
        ),
        migrations.AlterField(
            model_name='stock',
            name='currency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock.currency'),
        ),
    ]
