# Generated by Django 3.2.2 on 2021-06-06 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_information'),
    ]

    operations = [
        migrations.CreateModel(
            name='storyData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('story', models.TextField()),
            ],
        ),
    ]