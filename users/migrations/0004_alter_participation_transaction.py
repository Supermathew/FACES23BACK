# Generated by Django 3.2.9 on 2022-02-06 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0005_alter_transaction_donation_amount'),
        ('users', '0003_auto_20220111_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participation',
            name='transaction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='participations', to='transactions.transaction'),
        ),
    ]
