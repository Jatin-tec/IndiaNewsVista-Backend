# Generated by Django 4.2.4 on 2023-11-06 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_news_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
