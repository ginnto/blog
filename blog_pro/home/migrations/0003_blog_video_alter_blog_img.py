# Generated by Django 4.1.7 on 2023-04-26 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_comment_blog_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videos'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='picture'),
        ),
    ]