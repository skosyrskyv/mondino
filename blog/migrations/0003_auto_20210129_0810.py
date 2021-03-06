# Generated by Django 3.1.5 on 2021-01-29 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_blogpage_public_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogthemes',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AddField(
            model_name='blogthemes',
            name='slug',
            field=models.SlugField(default='', max_length=80, unique=True),
            preserve_default=False,
        ),
    ]
