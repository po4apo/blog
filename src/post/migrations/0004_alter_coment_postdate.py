# Generated by Django 3.2.5 on 2021-08-04 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_coment_postdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coment',
            name='postDate',
            field=models.DateTimeField(verbose_name='Дата публикации'),
        ),
    ]