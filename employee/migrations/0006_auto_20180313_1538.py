# Generated by Django 2.0.2 on 2018-03-13 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_expensedetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expensedetails',
            name='receipt',
            field=models.FileField(upload_to='media'),
        ),
    ]
