# Generated by Django 4.0.6 on 2022-07-29 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sigpotapp', '0005_delete_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Check',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu', models.CharField(max_length=200)),
                ('meal_time', models.CharField(max_length=200)),
            ],
        ),
    ]
