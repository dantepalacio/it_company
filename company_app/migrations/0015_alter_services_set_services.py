# Generated by Django 4.2.1 on 2023-05-14 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company_app', '0014_services_set_services_alter_news_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='services',
            name='set_services',
            field=models.IntegerField(choices=[(1, 'Веб разработка'), (2, 'Мобильная разработка'), (3, 'Маркетинг')], null=True),
        ),
    ]