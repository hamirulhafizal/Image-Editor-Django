# Generated by Django 2.2.13 on 2020-06-21 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0004_auto_20200621_0857'),
    ]

    operations = [
        migrations.CreateModel(
            name='Myimage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('thumbnail', models.ImageField(upload_to='')),
            ],
        ),
    ]
