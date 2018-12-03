# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-03 14:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20181203_1503'),
    ]

    operations = [
        migrations.RenameField(
            model_name='depot_to_costumer_shipping',
            old_name='costumer_fk',
            new_name='customer_fk',
        ),
        migrations.RenameField(
            model_name='factory_to_costumer_shipping',
            old_name='costumer_fk',
            new_name='customer_fk',
        ),
        migrations.AlterUniqueTogether(
            name='depot_to_costumer_shipping',
            unique_together=set([('depot_fk', 'customer_fk')]),
        ),
        migrations.AlterUniqueTogether(
            name='factory_to_costumer_shipping',
            unique_together=set([('factory_fk', 'customer_fk')]),
        ),
    ]