# Generated by Django 4.2.1 on 2023-05-14 17:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_app', '0012_alter_communication_city_phone_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutcompany',
            options={'verbose_name': 'компания туралы', 'verbose_name_plural': 'компания туралы'},
        ),
        migrations.AlterModelOptions(
            name='communication',
            options={'verbose_name': 'байланыс', 'verbose_name_plural': 'байланыс'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'байланыс', 'verbose_name_plural': 'байланыстар'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'жаңалықтар', 'verbose_name_plural': 'жаңалықтар'},
        ),
        migrations.AlterModelOptions(
            name='projects',
            options={'verbose_name': 'жоба', 'verbose_name_plural': 'жобалар'},
        ),
        migrations.AlterModelOptions(
            name='services',
            options={'verbose_name': 'қызмет', 'verbose_name_plural': 'қызметтер'},
        ),
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='news_image'),
        ),
        migrations.AlterField(
            model_name='aboutcompany',
            name='text',
            field=models.TextField(verbose_name='сипаттамасы'),
        ),
        migrations.AlterField(
            model_name='communication',
            name='adress',
            field=models.CharField(max_length=255, verbose_name='мекенжайы'),
        ),
        migrations.AlterField(
            model_name='communication',
            name='city_phone',
            field=models.CharField(max_length=15, null=True, validators=[django.core.validators.RegexValidator(message="Телефон нөмірі келесі форматта болуы керек: '+7-7212-XX-XX-XX'.", regex='^\\+7-\\d{4}-\\d{2}-\\d{2}-\\d{2}$')], verbose_name='қалалық телефон'),
        ),
        migrations.AlterField(
            model_name='communication',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='электрондық пошта'),
        ),
        migrations.AlterField(
            model_name='communication',
            name='location',
            field=models.CharField(max_length=55, verbose_name='орналасуы'),
        ),
        migrations.AlterField(
            model_name='communication',
            name='phone',
            field=models.CharField(max_length=15, null=True, validators=[django.core.validators.RegexValidator(message="Телефон нөмірі келесі форматта болуы керек: '+7-7XX-XXX-XX-XX'.", regex='^\\+7-\\d{3}-\\d{3}-\\d{2}-\\d{2}$')], verbose_name='телефон нөмірі'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='электрондық пошта'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='аты'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name='тегі'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(verbose_name='хабар'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='status',
            field=models.CharField(choices=[('pending', 'қарастырылып отырған'), ('reviewed', 'қаралды')], default='қарастырылып отырған', max_length=10, verbose_name='мәртебесі'),
        ),
        migrations.AlterField(
            model_name='news',
            name='data',
            field=models.DateTimeField(auto_now_add=True, verbose_name='деректер'),
        ),
        migrations.AlterField(
            model_name='news',
            name='info',
            field=models.TextField(max_length=5000, verbose_name='сипаттамасы'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=50, verbose_name='тақырып'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='area',
            field=models.CharField(max_length=50, verbose_name='қызмет саласы'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='client',
            field=models.CharField(max_length=50, verbose_name='клиент'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='description',
            field=models.TextField(verbose_name='сипаттамасы'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='image',
            field=models.ImageField(upload_to='project_image', verbose_name='сурет'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='name',
            field=models.CharField(max_length=255, verbose_name='тақырып'),
        ),
        migrations.AlterField(
            model_name='services',
            name='name',
            field=models.CharField(max_length=255, verbose_name='тақырып'),
        ),
        migrations.AlterField(
            model_name='services',
            name='price',
            field=models.PositiveIntegerField(blank=True, verbose_name='бағасы'),
        ),
    ]
