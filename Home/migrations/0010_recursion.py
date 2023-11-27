# Generated by Django 4.2.4 on 2023-08-08 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0009_auto_20230807_1547'),
    ]

    operations = [
        migrations.CreateModel(
            name='recursion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.CharField(default='1', max_length=20)),
                ('name', models.CharField(max_length=90)),
                ('description', models.TextField(default='Do it yourself!', max_length=250)),
                ('link', models.URLField()),
            ],
        ),
    ]