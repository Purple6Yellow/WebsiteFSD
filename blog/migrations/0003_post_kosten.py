# Generated by Django 3.2.22 on 2023-11-03 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20231103_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Kosten',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True),
        ),
    ]
