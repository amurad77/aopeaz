# Generated by Django 3.2.16 on 2022-11-22 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='media/pdf', verbose_name='Pdf faylı'),
        ),
        migrations.AlterField(
            model_name='news',
            name='pdf_title',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Pdf faylının adı'),
        ),
    ]
