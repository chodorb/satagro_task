from django.core.management.base import BaseCommand
from django.contrib.gis.geos import Point

from techlines.models import TechLine
from fields.models import Field

import uuid
import requests

class Command(BaseCommand):
    help = "Fetch sample techlines from api"
    
    def handle(self,*args,**options):
        
        field_id = 'cbf7bb1d-c5b1-4dfa-83d2-5800f78ffb8d'
        field_name = 'Sample Field'
        
        field = Field(id=uuid.UUID(field_id), name = field_name)
        
        if not Field.objects.filter(id=uuid.UUID(field_id)).exists():
            field.save()
            techlines_data = requests.get(f"https://mocki.io/v1/{field_id}").json()
            
            for value in techlines_data['values']:
                techline = TechLine.objects.create(
                    type = value['type'],
                    heading = value['heading'],
                    aPoint = Point(value['aPoint']['lon'],value['aPoint']['lat']),
                    bPoint = Point(value['bPoint']['lon'],value['bPoint']['lat']),
                    archived = value['archived'],
                    field = field
                )
                
                techline.lastModfiedTime = value['lastModifiedTime']
                techline.save()
            
                
                self.stdout.write(f'Techline {techline.id} added to {field.id}')
        else:
            self.stdout.write(self.style.WARNING("Data already fetched"))
        