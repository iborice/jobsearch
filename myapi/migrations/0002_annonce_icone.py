# Generated by Django 3.2.4 on 2021-09-21 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='annonce',
            name='icone',
            field=models.ImageField(default='myapi/static/myapi/default.jpg', upload_to='myapi/static/myapi/icones/'),
        ),
    ]