# Generated by Django 3.1.5 on 2021-05-13 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CrowdSource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=300, null=True)),
                ('location', models.TextField(blank=True, max_length=1000, null=True)),
                ('contact', models.CharField(blank=True, max_length=300, null=True)),
                ('desc', models.TextField(blank=True, max_length=3000, null=True)),
                ('person_name', models.CharField(blank=True, max_length=300, null=True)),
                ('person_email', models.CharField(blank=True, max_length=300, null=True)),
                ('person_contact', models.CharField(blank=True, max_length=10, null=True)),
                ('reviewed', models.BooleanField(blank=True, null=True)),
                ('sub_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bookbank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True)),
                ('address', models.TextField(blank=True, max_length=50000, null=True)),
                ('contact', models.CharField(blank=True, max_length=150, null=True)),
                ('updated_on', models.DateField(auto_now=True)),
                ('site_url', models.CharField(blank=True, max_length=300, null=True)),
                ('content', models.TextField(blank=True, max_length=50000, null=True)),
                ('slug', models.SlugField(blank=True, max_length=150)),
                ('books', models.ManyToManyField(to='bookbanks.Books')),
                ('district', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='bookbanks.district')),
                ('state', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='bookbanks.state')),
            ],
        ),
    ]
