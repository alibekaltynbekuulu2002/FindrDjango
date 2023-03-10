# Generated by Django 4.1.7 on 2023-03-09 18:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_useraddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('MALE', 'M'), ('FEMALE', 'F')], default=None, max_length=20, null=True),
        ),
        migrations.CreateModel(
            name='UserPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_type', models.CharField(choices=[('Visa', 'Visa'), ('Cash', 'Cash')], default='Cash', max_length=20)),
                ('provider', models.CharField(blank=True, max_length=50, null=True)),
                ('account_no', models.CharField(blank=True, max_length=50, null=True)),
                ('expiry', models.CharField(blank=True, max_length=10, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_payments',
            },
        ),
    ]
