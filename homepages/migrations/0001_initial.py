# Generated by Django 4.0 on 2022-02-08 17:21

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='static/uploads')),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200, null=True, validators=[django.core.validators.MinLengthValidator(2)])),
                ('category_info', models.TextField()),
                ('category_image', models.FileField(null=True, upload_to='static/category_uploads')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('product_price', models.FloatField()),
                ('product_image', models.FileField(upload_to='static/product_uploads')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='homepages.productcategory')),
            ],
        ),
        migrations.CreateModel(
            name='SendFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, null=True, validators=[django.core.validators.EmailValidator()])),
                ('subject', models.CharField(max_length=10)),
                ('message', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepages.productlist')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(1000)])),
                ('total_price', models.IntegerField(null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Delivered', 'Delivered')], max_length=200, null=True)),
                ('payment_method', models.CharField(choices=[('Cash On Delivery', 'Cash On Delivery'), ('Esewa', 'Esewa'), ('Khalti', 'Khalti')], max_length=200, null=True)),
                ('payment_status', models.BooleanField(blank=True, default=False, null=True)),
                ('contact_no', models.CharField(max_length=10, null=True, validators=[django.core.validators.MinLengthValidator(9), django.core.validators.MaxLengthValidator(10)])),
                ('contact_address', models.CharField(max_length=200, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='homepages.productlist')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepages.productlist')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
