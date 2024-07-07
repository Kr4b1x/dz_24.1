# Generated by Django 4.2.13 on 2024-07-07 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='total_sum',
        ),
        migrations.AddField(
            model_name='payment',
            name='payment_link',
            field=models.URLField(blank=True, max_length=400, null=True, verbose_name='ссылка на оплату'),
        ),
        migrations.AddField(
            model_name='payment',
            name='session_id',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='ID сессии'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_method',
            field=models.CharField(default='card', max_length=20, verbose_name='способ оплаты'),
        ),
    ]
