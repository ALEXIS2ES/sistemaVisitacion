# Generated by Django 2.2.7 on 2019-11-27 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visita', '0003_auto_20191127_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitador',
            name='pdf',
            field=models.FileField(blank=True, default=None, null=True, unique=True, upload_to='pdf/'),
        ),
    ]
