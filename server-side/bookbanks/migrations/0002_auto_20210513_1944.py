# Generated by Django 3.1.5 on 2021-05-13 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookbanks', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookbank',
            options={'verbose_name_plural': 'Bookbank'},
        ),
        migrations.AlterModelOptions(
            name='books',
            options={'verbose_name_plural': 'Books'},
        ),
        migrations.AlterModelOptions(
            name='crowdsource',
            options={'verbose_name_plural': 'CrowdSource'},
        ),
        migrations.AlterModelOptions(
            name='district',
            options={'verbose_name_plural': 'District'},
        ),
        migrations.AlterModelOptions(
            name='state',
            options={'verbose_name_plural': 'State'},
        ),
    ]
