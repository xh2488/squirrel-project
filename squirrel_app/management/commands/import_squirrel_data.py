from django.core.management.base import BaseCommand
from squirrel_app.models import squirrel_info
import csv
import pandas as pd

class Command(BaseCommand):
    help = 'Populate database'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help='Indicates the path of dataset to be created')

    def handle(self, *args, **kwargs):
        file_path = kwargs['path']
        print(file_path)
        df = pd.read_csv(file_path)
        #df['Date'] = pd.to_datetime(df['Date'])
        # df = df.dropna()
        print(len(df) - df.count())
        squirrel_info_list = [squirrel_info(
            Longtitude=row['X'],
            Latitude=row['Y'],
            Unique_Squirrel_ID=row['Unique Squirrel ID'],
            Hectare=row['Hectare'],
            Shift=row['Shift'],
            Date=row['Date'],
            Hectare_squirrel_number=row['Hectare Squirrel Number'],
            Age=row['Age'],
            Primary_fur_color=row['Primary Fur Color'],
            Highlight_fur_color=row['Highlight Fur Color'],
            combination_color=row['Combination of Primary and Highlight Color'],
            Color_notes=row['Color notes'],
            Location=row['Location'],
            Specific_location=row['Specific Location'],
            Running=row['Running'],
            Chasing=row['Chasing'],
            Climbing=row['Climbing'],
            Eating=row['Eating'],
            Foraging=row['Foraging'],
            Kuks=row['Kuks'],
            Quaas=row['Quaas'],
            Moans=row['Moans'],
            Tail_flags=row['Tail flags'],
            Tail_twitches=row['Tail twitches'],
            Approaches=row['Approaches'],
            Indifferent=row['Indifferent'],
            Runs_from=row['Runs from'],
            Other_activities=row['Other Activities']

        ).save()
            for index, row in df.iterrows()
        ]
        
        print(df.dtypes)
        # squirrel_info.objects.bulk_create(squirrel_info_list)
        print("saved to db")
        # with open(file_path, 'rt') as csv_file:
        #     reader = csv.reader(csv_file, delimiter=',', quotechar='|')
        #     # header = reader.next()
        #     for row in reader:

        #
        #         print(row)
        #         break
                # _object_dict = {key: value for key, value in zip(header, row)}
                # _model.objects.create(**_object_dict)
