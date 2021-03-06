# Generated by Django 3.2 on 2021-04-08 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squirrel_app', '0002_auto_20210408_0529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrel_info',
            name='Age',
            field=models.CharField(blank=True, help_text='Age, either Adult or Juvenile', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel_info',
            name='Date',
            field=models.CharField(blank=True, help_text='Sighting session date', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel_info',
            name='Location',
            field=models.CharField(blank=True, help_text='location of the squirrel, either Ground Plane or Above Ground ', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel_info',
            name='Other_activities',
            field=models.CharField(blank=True, help_text='If there is any other types of interactions between squirrels and humans', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel_info',
            name='Primary_fur_color',
            field=models.CharField(blank=True, help_text='The primary fur color of the squirrels', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel_info',
            name='Shift',
            field=models.CharField(blank=True, help_text='Whether the sighting session occurred in the morning or afternoon', max_length=50, null=True),
        ),
    ]
