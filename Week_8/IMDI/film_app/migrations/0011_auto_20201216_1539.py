# Generated by Django 3.1.4 on 2020-12-16 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film_app', '0010_auto_20201216_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='available_in_countries',
            field=models.ManyToManyField(related_name='film_aviaible_country', to='film_app.Country'),
        ),
    ]
