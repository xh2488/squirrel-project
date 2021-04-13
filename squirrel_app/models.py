from django.db import models
from django.utils.translation import gettext as _
from django.forms import ModelForm




# Create your models here.

class squirrel_info(models.Model):
    Longtitude = models.FloatField(
        max_length=50,
        help_text= _('Squirrel longtitude'),
        null=True,
        blank=True,
    )

    Latitude = models.FloatField(
        max_length=50,
        help_text=_('Squirrel latitude'),
        null=True,
        blank=True,
    )

    Unique_Squirrel_ID = models.CharField(
        max_length=50,
        help_text=_('The unique ID of the squirrel'),
        null=True,
        blank=True,
    )



    Hectare = models.CharField(
        max_length=50,
        help_text=_('Hector grid ID'),
        null=True,
        blank=True,
    )

    AM = 'AM'
    PM = 'PM'
    SHIFT_CHOICE = [
        (AM,_('AM')),
        (PM,_('PM')),
    ]


    Shift = models.CharField(
        max_length=50,
        help_text=_('Whether the sighting session occurred in the morning or afternoon'),
        choices=SHIFT_CHOICE,
        null=True,
        blank=True,
    )

    Date = models.CharField(
        max_length=50,
        help_text='Sighting session date',
        null=True,
        blank=True,
    )

    Hectare_squirrel_number = models.IntegerField(
        help_text=_('Number within the chronological sequence of squirrel sightings for a discrete sighting session'),
        null=True,
    )

    ADULT = "Adult"
    JUVENILE = 'Juvenile'

    AGE_CHOICE = [
        (ADULT,_('Adult')),
        (JUVENILE,_('Juvenile')),
    ]

    Age = models.CharField(
        max_length=50,
        help_text='Age, either Adult or Juvenile',
        choices=AGE_CHOICE,
        null=True,
        blank=True,
    )

    GRAY = 'Gray'
    CINNAMON = 'Cinnamon'
    BLACK = 'Black'

    COLOR_CHOICE = [
        (GRAY, _('Gray')),
        (CINNAMON,_('Cinnamon')),
        (BLACK,_('Black')),
    ]

    Primary_fur_color = models.CharField(
        max_length=50,
        help_text='The primary fur color of the squirrels',
        choices=COLOR_CHOICE,
        null=True,
        blank=True,
    )

    Highlight_fur_color = models.CharField(
        max_length=50,
        help_text='The highlight fur color of the squirrels',
        null=True,
        blank=True,
    )

    combination_color = models.CharField(
        max_length=50,
        help_text='Permutations of primary and highlight colors observed',
        null=True,
        blank=True,
    )

    Color_notes = models.CharField(
        max_length=50,
        help_text='commentary on the squirrel ',
        null=True,
        blank=True,
    )

    ABOVE_GROUND = 'Above Ground'
    GROUND_PLANE = 'Ground Plane'

    LOCATION_CHOICE = [
        (ABOVE_GROUND,_('Above Ground')),
        (GROUND_PLANE,_('Ground Plane')),

    ]

    Location = models.CharField(
        max_length=50,
        help_text='Location of the squirrel, either Ground Plane or Above Ground ',
        # choices=LOCATION_CHOICE,
        null=True,
        blank=True,
    )

    Specific_location = models.CharField(
        max_length=50,
        help_text='Specific location of the squirrel ',
        null=True,
        blank=True,
    )

    Running = models.BooleanField(
        help_text=_('If the squirrel is seen running'),
        null=True,
        blank=True,
    )

    Chasing = models.BooleanField(
        help_text=_('If the squirrel is seen chasing'),
        null=True,
        blank=True,
    )

    Climbing = models.BooleanField(
        help_text=_('If the squirrel is seen climbing'),
        null=True,
        blank=True,
    )

    Eating = models.BooleanField(
        help_text=_('If the squirrel is seen eating'),
        null=True,
        blank=True,
    )

    Foraging = models.BooleanField(
        help_text=_('If the squirrel is seen foraging'),
        null=True,
        blank=True,
    )

    Kuks = models.BooleanField(
        help_text=_('If the squirrel is heard kukking'),
        null=True,
        blank=True,
    )


    Quaas = models.BooleanField(
        help_text=_('If the squirrel is heard quaaing'),
        null=True,
        blank=True,
    )

    Moans = models.BooleanField(
        help_text=_('If the squirrel is heard moaning'),
        null=True,
        blank=True,
    )

    Tail_flags = models.BooleanField(
        help_text=_('If the squirrel is seen flagging its tail'),
        null=True,
        blank=True,
    )
    Tail_twitches = models.BooleanField(
        help_text=_('If the squirrel is seen twitching its tail'),
        null=True,
        blank=True,
    )

    Approaches = models.BooleanField(
        help_text=_('If the squirrel is seen approaching peoplel'),
        null=True,
        blank=True,
    )

    Indifferent = models.BooleanField(
        help_text=_('If the squirrel is indifferent to human presence'),
        null=True,
        blank=True,
    )

    Runs_from = models.BooleanField(
        help_text=_('If the squirrel is running from human'),
        null=True,
        blank=True,
    )

    Other_activities = models.CharField(
        help_text=_('If there is any other types of interactions between squirrels and humans'),
        null=True,
        blank=True,
        max_length=50,
    )

class AddSquirrelForm(ModelForm):
    class Meta:
        model = squirrel_info
        fields = ['Longtitude', "Latitude", "Unique_Squirrel_ID", "Shift", "Date", "Age", "Primary_fur_color", "Location", "Specific_location", "Running", "Chasing", "Climbing", "Eating", "Foraging", "Other_activities", "Kuks", "Quaas", "Moans", "Tail_flags", "Tail_twitches", "Approaches", "Indifferent", "Runs_from"]















