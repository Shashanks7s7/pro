# Generated by Django 4.0.1 on 2022-01-17 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_team_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('message', models.TextField()),
                ('senderemail', models.EmailField(max_length=254)),
            ],
        ),
    ]
