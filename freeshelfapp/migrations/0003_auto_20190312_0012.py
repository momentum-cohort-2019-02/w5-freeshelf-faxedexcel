# Generated by Django 2.1.7 on 2019-03-12 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freeshelfapp', '0002_auto_20190312_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(blank=True, max_length=2000, null=True),
        ),
    ]
