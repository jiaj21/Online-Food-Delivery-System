# Generated by Django 4.2.7 on 2023-11-19 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_address_book_address_type_and_more'),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='cust_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.customer'),
        ),
    ]
