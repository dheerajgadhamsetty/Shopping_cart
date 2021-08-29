# Generated by Django 3.2.4 on 2021-07-24 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Garments', '0004_auto_20210723_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='formalshirt',
            field=models.ForeignKey(default='True', on_delete=django.db.models.deletion.CASCADE, to='Garments.formalshirt'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='tr',
            field=models.ForeignKey(default='True', on_delete=django.db.models.deletion.CASCADE, to='Garments.trousers'),
        ),
    ]
