# Generated by Django 5.0 on 2023-12-17 19:46

import django.db.models.deletion
import myapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('batch_id', models.IntegerField(primary_key=True, serialize=False)),
                ('time', models.CharField(choices=[('M1', '6-7 AM'), ('M2', '7-8 AM'), ('M3', '8-9 AM'), ('E', '5-6 PM')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('age', models.PositiveIntegerField(validators=[myapp.models.validate_age])),
                ('email', models.EmailField(max_length=50, unique='True')),
                ('contact_number', models.CharField(blank=True, max_length=10, unique='True')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.batch')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('payment_id', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.PositiveIntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('payment_successful', models.BooleanField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('admission_id', models.AutoField(primary_key=True, serialize=False)),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.batch')),
                ('payment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.payment')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
    ]
