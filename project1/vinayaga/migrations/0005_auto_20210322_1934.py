# Generated by Django 3.1.6 on 2021-03-22 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vinayaga', '0004_detail_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detail',
            name='Image',
        ),
        migrations.AddField(
            model_name='detail',
            name='Image1',
            field=models.ImageField(default='', upload_to='images1/'),
        ),
        migrations.AddField(
            model_name='detail',
            name='Image2',
            field=models.ImageField(default='', upload_to='images2/'),
        ),
        migrations.AddField(
            model_name='detail',
            name='Image3',
            field=models.ImageField(default='', upload_to='images3/'),
        ),
        migrations.AddField(
            model_name='detail',
            name='Image4',
            field=models.ImageField(default='', upload_to='images4/'),
        ),
        migrations.AddField(
            model_name='detail',
            name='Image5',
            field=models.ImageField(default='', upload_to='images5/'),
        ),
    ]
