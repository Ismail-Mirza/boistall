# Generated by Django 3.2.4 on 2022-03-12 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newProduct', '0011_merge_20220221_1557'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brand',
            options={'ordering': ('-brand',)},
        ),
    ]