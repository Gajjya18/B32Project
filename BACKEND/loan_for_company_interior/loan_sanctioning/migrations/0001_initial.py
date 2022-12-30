# Generated by Django 4.1.4 on 2022-12-19 19:26

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('application_generation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=0, max_length=250)),
                ('vendor_type', models.CharField(blank=True, default=0, max_length=250)),
                ('email', models.EmailField(blank=True, default=0, max_length=254)),
                ('address', models.TextField(blank=True, default=0, max_length=250)),
                ('city', models.CharField(blank=True, default=0, max_length=250)),
                ('state', models.CharField(blank=True, default=0, max_length=250)),
                ('country', models.CharField(blank=True, default=0, max_length=250)),
                ('pin_code', models.IntegerField(blank=True, default=0)),
                ('mobile', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='IN')),
                ('bank_name', models.CharField(blank=True, default=0, max_length=250)),
                ('passbook_copy', models.FileField(blank=True, default=0, upload_to='customer/vendor/')),
                ('current_account_no', models.CharField(blank=True, default=0, max_length=25)),
                ('ifsc_code', models.CharField(blank=True, default=0, max_length=20)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Vendors', to='application_generation.application')),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_principal_amount', models.FloatField(blank=True, default=0)),
                ('loan_tenure', models.FloatField(blank=True, default=0)),
                ('interest_rate', models.FloatField(blank=True, default=0)),
                ('total_amount_and_processing_fees', models.FloatField(blank=True, default=0)),
                ('installment', models.IntegerField(blank=True, default=0)),
                ('maturity_date', models.DateField(blank=True, default='2000-12-12')),
                ('sanction_letter', models.FileField(blank=True, default=0, upload_to='customer/loan/')),
                ('status', models.CharField(blank=True, choices=[('SELECT', 'SELECT'), ('PENDING', 'PENDING'), ('DONE', 'DONE'), ('REJECTED', 'REJECTED')], default=0, max_length=250)),
                ('response_timestamp', models.DateTimeField(auto_now=True)),
                ('remark', models.CharField(blank=True, default=0, max_length=250)),
                ('application', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Loans', to='application_generation.application')),
            ],
        ),
    ]
