# Generated by Django 4.2.4 on 2023-09-21 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('ordering', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['ordering'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/images')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='products/thumbs')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendor.vendor')),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
    ]
