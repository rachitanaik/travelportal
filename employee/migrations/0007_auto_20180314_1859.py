# Generated by Django 2.0.2 on 2018-03-14 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0006_auto_20180313_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='expensedetails',
            name='approval',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='traveldetails',
            name='approval',
            field=models.CharField(max_length=5, null=True),
        ),
    ]
