# Generated by Django 3.1.5 on 2021-05-13 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ngo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Category'},
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name_plural': 'Country'},
        ),
        migrations.AlterModelOptions(
            name='crowdsource',
            options={'verbose_name_plural': 'CrowdSource'},
        ),
        migrations.AlterModelOptions(
            name='gender',
            options={'verbose_name_plural': 'Gender'},
        ),
        migrations.AlterModelOptions(
            name='ngo',
            options={'verbose_name_plural': 'NGO'},
        ),
        migrations.AlterModelOptions(
            name='religion',
            options={'verbose_name_plural': 'Religion'},
        ),
        migrations.AlterModelOptions(
            name='state',
            options={'verbose_name_plural': 'State'},
        ),
        migrations.AlterModelOptions(
            name='type',
            options={'verbose_name_plural': 'Type'},
        ),
    ]
