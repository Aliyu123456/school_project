# Generated by Django 4.2.16 on 2025-03-14 16:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=200)),
                ('crop_name', models.CharField(max_length=100)),
                ('crop_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('crop_desc', models.TextField()),
                ('available', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('crop_img', models.ImageField(upload_to='img/products_img')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='crops', to='products.category')),
                ('farmer', models.ForeignKey(limit_choices_to={'role': 'farmer'}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('crop_name',),
                'index_together': {('id', 'slug')},
            },
        ),
    ]
