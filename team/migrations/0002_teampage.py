# Generated by Django 3.1.5 on 2021-01-29 06:53

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0059_apply_collection_ordering'),
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('team_slider', wagtail.core.fields.StreamField([('image', wagtail.images.blocks.ImageChooserBlock(icon='image'))], blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]