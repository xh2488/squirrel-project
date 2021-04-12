import csv
from django.core.management.base import BaseCommand
from squirrel_app.models import squirrel_info

class Command(BaseCommand):
    help = 'Populate database'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help='Indicates the path of dataset to be created')

    def handle(self, *args, **kwargs):
        file_path = kwargs['path']
        f = open(file_path, 'w+')
        writer = csv.writer(f)
        fields_list = squirrel_info._meta.fields
        fields_list = [i.name for i in fields_list][1:]
        writer.writerow(fields_list)
        for obj in squirrel_info.objects.all():
            row = [getattr(obj, field) for field in fields_list]
            writer.writerow(row)
        f.close()


