# Generated by Django 3.1.5 on 2021-02-01 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarships', '0002_auto_20210201_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scholarship',
            name='s_about',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
