# Generated by Django 2.2 on 2020-03-23 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_articulo_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('logo', models.ImageField(null=True, upload_to='logos')),
                ('slogan', models.CharField(max_length=200, null=True)),
                ('facebook', models.URLField(null=True)),
                ('instagram', models.URLField(null=True)),
                ('color_primario', models.CharField(default='#000000', max_length=7)),
                ('color_secundario', models.CharField(default='#FFFFFF', max_length=7)),
            ],
        ),
    ]
