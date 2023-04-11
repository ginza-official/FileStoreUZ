# Generated by Django 3.2.6 on 2022-04-09 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='kitob', max_length=300, null=True)),
                ('title', models.TextField(blank=True, default='filestore.uz', null=True)),
                ('img', models.ImageField(default='books/img/img.jpg', upload_to='books/img')),
                ('file', models.FileField(default='books/file/file.pdf', upload_to='books/file')),
                ('coin', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('download_count', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('created_data', models.DateField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
            ],
        ),
    ]
