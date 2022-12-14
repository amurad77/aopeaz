# Generated by Django 4.1.3 on 2022-11-21 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/news', verbose_name='Əsas Şəkil')),
                ('title', models.CharField(max_length=256, verbose_name='Başlıq')),
                ('title_az', models.CharField(max_length=256, null=True, verbose_name='Başlıq')),
                ('title_en', models.CharField(max_length=256, null=True, verbose_name='Başlıq')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='media/news', verbose_name='Şəkil1')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='media/news', verbose_name='Şəkil2')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='media/news', verbose_name='Şəkil3')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='media/news', verbose_name='Şəkil4')),
                ('image5', models.ImageField(blank=True, null=True, upload_to='media/news', verbose_name='Şəkil5')),
                ('description1', models.TextField(max_length=2000, verbose_name='Qısa məzmun')),
                ('description1_az', models.TextField(max_length=2000, null=True, verbose_name='Qısa məzmun')),
                ('description1_en', models.TextField(max_length=2000, null=True, verbose_name='Qısa məzmun')),
                ('description2', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Məzmun1')),
                ('description2_az', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Məzmun1')),
                ('description2_en', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Məzmun1')),
                ('description3', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Məzmun2')),
                ('description3_az', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Məzmun2')),
                ('description3_en', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Məzmun2')),
                ('description4', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Məzmun3')),
                ('description4_az', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Məzmun3')),
                ('description4_en', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Məzmun3')),
                ('description5', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Məzmun4')),
                ('description5_az', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Məzmun4')),
                ('description5_en', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Məzmun4')),
                ('pdf_title', models.CharField(max_length=256, verbose_name='Pdf adı')),
                ('pdf', models.FileField(blank=True, upload_to='media/pdf')),
                ('slug', models.SlugField(editable=False, max_length=256, unique=True, verbose_name='Slug')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
