# Generated by Django 5.1.5 on 2025-02-06 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=221)),
                ('second_name', models.CharField(max_length=221)),
                ('email', models.EmailField(max_length=221)),
                ('phone', models.CharField(max_length=221)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
