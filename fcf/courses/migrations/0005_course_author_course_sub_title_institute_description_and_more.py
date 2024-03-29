# Generated by Django 4.0.6 on 2022-12-30 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_course_img_institute_img_provider_img_university_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='author',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='course',
            name='sub_title',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AddField(
            model_name='institute',
            name='description',
            field=models.CharField(default='', max_length=10000),
        ),
        migrations.AddField(
            model_name='provider',
            name='description',
            field=models.CharField(default='', max_length=10000),
        ),
        migrations.AddField(
            model_name='sub_subject',
            name='description',
            field=models.CharField(default='', max_length=10000),
        ),
        migrations.AddField(
            model_name='sub_subject',
            name='img',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AddField(
            model_name='university',
            name='description',
            field=models.CharField(default='', max_length=10000),
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.CharField(max_length=10000),
        ),
    ]
