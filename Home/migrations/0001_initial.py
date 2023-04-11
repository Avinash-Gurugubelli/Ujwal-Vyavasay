# Generated by Django 4.1.7 on 2023-04-10 17:12

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('Name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
                ('adress', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=10, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator('^[0-9]{10}$', 'country code is not required')])),
                ('pinCode', models.CharField(max_length=6, validators=[django.core.validators.RegexValidator('^[0-9]{6}$', 'Invalid postal code')])),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pName', models.CharField(max_length=20)),
                ('price', models.FloatField(max_length=5)),
                ('maxQty', models.FloatField(max_length=5)),
                ('dTime', models.DateTimeField()),
                ('PImage', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('phone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.register')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quant', models.FloatField(max_length=5)),
                ('sPrc', models.FloatField(max_length=5)),
                ('aTime', models.DateTimeField()),
                ('pImage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pImage+', to='Home.upload')),
                ('pName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pName+', to='Home.upload')),
                ('phone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='Home.register')),
            ],
        ),
    ]
