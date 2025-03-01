# Generated by Django 5.1.4 on 2025-01-31 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='DayEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('last_transaction_price', models.FloatField(blank=True, null=True)),
                ('max_price', models.FloatField(blank=True, null=True)),
                ('min_price', models.FloatField(blank=True, null=True)),
                ('avg_price', models.FloatField(blank=True, null=True)),
                ('percentage', models.FloatField(blank=True, null=True)),
                ('profit', models.FloatField(blank=True, null=True)),
                ('total_profit', models.FloatField(blank=True, null=True)),
                ('company_code', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['date'],
                'unique_together': {('company_code', 'date')},
            },
        ),
        migrations.CreateModel(
            name='DayEntryAsString',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('date_string', models.CharField(blank=True, max_length=50, null=True)),
                ('last_transaction_price', models.CharField(blank=True, max_length=50, null=True)),
                ('max_price', models.CharField(blank=True, max_length=50, null=True)),
                ('min_price', models.CharField(blank=True, max_length=50, null=True)),
                ('avg_price', models.CharField(blank=True, max_length=50, null=True)),
                ('percentage', models.CharField(blank=True, max_length=50, null=True)),
                ('profit', models.CharField(blank=True, max_length=50, null=True)),
                ('total_profit', models.CharField(blank=True, max_length=50, null=True)),
                ('company_code', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['date'],
                'unique_together': {('company_code', 'date')},
            },
        ),
    ]
