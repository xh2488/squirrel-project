# Generated by Django 3.2 on 2021-04-11 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squirrel_app', '0005_auto_20210411_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrel_info',
            name='Age',
            field=models.CharField(blank=True, choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile')], help_text='Age, either Adult or Juvenile', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel_info',
            name='Primary_fur_color',
            field=models.CharField(blank=True, choices=[('Gray', 'Gray'), ('Cinnamon', 'Cinnamon'), ('Black', 'Black')], help_text='The primary fur color of the squirrels', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel_info',
            name='Shift',
            field=models.CharField(blank=True, choices=[('AM', 'AM'), ('PM', 'PM')], help_text='Whether the sighting session occurred in the morning or afternoon', max_length=50, null=True),
        ),
    ]