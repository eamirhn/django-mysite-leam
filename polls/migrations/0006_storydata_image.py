# Generated by Django 3.2.2 on 2021-07-24 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_storydata_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='storydata',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='%Y/%m/%d'),
        ),
    ]
