# Generated by Django 5.0 on 2024-09-11 15:29

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(max_length=30000)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('draft', models.BooleanField(default=True)),
            ],
        ),
    ]
