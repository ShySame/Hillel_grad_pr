# Generated by Django 3.2.8 on 2021-11-08 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockroom', '0003_alter_book_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='ISBN',
            field=models.CharField(max_length=17),
        ),
    ]
