# Generated by Django 3.1.2 on 2020-10-18 04:23

from django.db import migrations, models
import django.db.models.deletion
import utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CafeteriaManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
                ('joined_date', models.DateField(max_length=255)),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DailyBalance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('date', models.DateField(unique=True)),
                ('opening_balance', models.FloatField(verbose_name='Opening Balance')),
                ('closing_balance', models.FloatField(verbose_name='Closing Balance')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('date', models.DateField()),
                ('sub_total', models.FloatField()),
                ('discount_amount', models.FloatField(default=0.0)),
                ('discount_percent', utils.fields.PercentField(default=0.0, verbose_name='Discount Percent')),
                ('service_tax', utils.fields.PercentField(default=0.0, verbose_name='Service Tax Percent')),
                ('net_total', models.FloatField()),
                ('is_sold_after_6_pm', models.BooleanField(default=False)),
                ('customer', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(choices=[('CASH', 'Cash'), ('CREDIT', 'Credit')], default='CASH', max_length=50, verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Income / Sale',
            },
        ),
        migrations.CreateModel(
            name='Particular',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('particular', models.CharField(max_length=255)),
                ('cost_unit_price', models.FloatField()),
                ('selling_unit_price', models.FloatField()),
                ('bought_for', models.CharField(choices=[('INPUT', 'Input'), ('OUTPUT', 'Output'), ('BOTH', 'Both')], default='OUTPUT', max_length=50, verbose_name='Purpose')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Penalty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('date', models.DateField()),
                ('party', models.CharField(max_length=255)),
                ('charge', models.FloatField()),
                ('is_fulfilled', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Penalty',
                'verbose_name_plural': 'Penalties',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('date', models.DateField()),
                ('party', models.CharField(max_length=255)),
                ('amount', models.FloatField()),
                ('is_expenditure', models.BooleanField(default=False, help_text="Click on checkbox for general expenditure and don't click for investment", verbose_name='Is Expenditure or not ?')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('item_remaining', models.PositiveIntegerField()),
                ('particular', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cafeteria.particular')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quantity', models.PositiveSmallIntegerField()),
                ('income', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='cafeteria.income')),
                ('particular', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cafeteria.particular')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Incentive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('date', models.DateField()),
                ('amount', models.FloatField(default=0)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cafeteria.cafeteriamanager')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('date', models.DateField()),
                ('quantity', models.PositiveSmallIntegerField()),
                ('total_price', models.FloatField()),
                ('bought_by', models.CharField(max_length=255)),
                ('bought_from', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('CASH', 'Cash'), ('CREDIT', 'Credit')], default='CASH', max_length=50, verbose_name='Status')),
                ('particular', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cafeteria.particular')),
            ],
            options={
                'verbose_name': 'Expense / Buying',
            },
        ),
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('date', models.DateField()),
                ('mark_as_cleared', models.BooleanField(default=False)),
                ('transaction', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cafeteria.income')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
