# Generated by Django 5.1.3 on 2024-12-01 04:46

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ColorVariant',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('color_name', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SizeVariant',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('size_name', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='product_description',
            new_name='product_desription',
        ),
        migrations.RemoveField(
            model_name='product',
            name='ription',
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='category_image',
            field=models.ImageField(upload_to='catgories'),
        ),
        migrations.AddField(
            model_name='product',
            name='color_variant',
            field=models.ManyToManyField(blank=True, to='products.colorvariant'),
        ),
        migrations.AddField(
            model_name='product',
            name='size_variant',
            field=models.ManyToManyField(blank=True, to='products.sizevariant'),
        ),
    ]
