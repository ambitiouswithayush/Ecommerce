# Generated by Django 5.1.3 on 2024-12-01 04:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_colorvariant_sizevariant_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_desription',
            new_name='product_description',
        ),
    ]