# Generated by Django 4.1.3 on 2022-11-17 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_news_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='pdf',
            field=models.FileField(blank=True, upload_to='media/pdf'),
        ),
    ]
