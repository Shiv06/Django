import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

## Fake Data script
import random
from faker import Faker
from first_app.models import AccessRecord,Topic,Webpage
fake_gen=Faker()

topic=['Search','Social','Marketplace','News','Games']

def add_topic():
    t=Topic.objects.get_or_create(top_name=random.choice(topic))[0]
    t.save()
    return t

def populate_web_Access(N=5):
    for x in range(N):
        topic=add_topic()

        ## generate fake data

        fake_name=fake_gen.company()
        fake_url=fake_gen.url()
        fake_date=fake_gen.date()

        webpage=Webpage.objects.get_or_create(topic=topic,name=fake_name,url=fake_url)[0]

        access_rec=AccessRecord.objects.get_or_create(webpageName=webpage,date=fake_date)[0]

if __name__ == '__main__':
    print('Populating data started')
    populate_web_Access(20)
    print('Populating data completed')
