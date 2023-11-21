# Generated by Django 4.2.7 on 2023-11-20 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_address_book_address_type_and_more'),
        ('order', '0006_cart_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='rider_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.delivery_agent'),
        ),
    ]