# Generated by Django 4.2.13 on 2024-07-03 22:20

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolio', '0002_contacto_mensaje_cifrado'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='contenido',
            field=ckeditor.fields.RichTextField(default=''),
            preserve_default=False,
        ),
    ]
