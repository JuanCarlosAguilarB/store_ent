# Generated by Django 4.0.6 on 2022-08-18 21:38

import apps.productos.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categorias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('imagen', models.ImageField(upload_to=apps.productos.models.product_directory_path)),
                ('video', models.FileField(blank=True, null=True, upload_to=apps.productos.models.product_directory_path)),
                ('descripcion', models.TextField()),
                ('precio', models.IntegerField()),
                ('cantidad', models.IntegerField()),
                ('published', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10)),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='categorias.categoria')),
            ],
            options={
                'ordering': ('-published',),
            },
        ),
    ]
