# Generated by Django 4.0.dev20210713072537 on 2021-08-12 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Words',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('English_word', models.CharField(max_length=30, unique=True)),
                ('Hebrew_word', models.CharField(max_length=30)),
                ('How_To_Remember', models.TextField(max_length=60)),
                ('Name', models.CharField(max_length=20, null=True)),
                ('pub_date', models.DateTimeField()),
            ],
        ),
    ]
