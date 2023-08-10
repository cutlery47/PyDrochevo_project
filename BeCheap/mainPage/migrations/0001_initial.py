# Generated by Django 4.2.3 on 2023-08-02 10:09

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
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('subscriptions', models.ManyToManyField(related_name='subscriptions_categories', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('item_brand', models.CharField(max_length=20)),
                ('item_cur_price', models.CharField(max_length=20)),
                ('item_prev_price', models.CharField(max_length=20)),
                ('item_link', models.URLField(max_length=300, null=True)),
                ('item_date', models.TimeField(auto_now=True)),
                ('item_image', models.URLField(max_length=300, null=True)),
                ('favorites', models.ManyToManyField(related_name='user', through='mainPage.Favorite', to=settings.AUTH_USER_MODEL)),
                ('item_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='mainPage.categories')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.AddField(
            model_name='favorite',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainPage.items'),
        ),
        migrations.AddField(
            model_name='favorite',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
