import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

#----------------------------------------------------
# Add new topics (manullay)
from first_app.models import AccessRecord, Webpage, Topic
import random
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']
def add_topic():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    t.save()
    return t
#----------------------------------------------------
# Population function, using fake dataset:

from faker import Faker
fakegen = Faker()

def populate(N=5):
    '''
    Create N Entries of Dates Accessed
    '''
    for entry in range(N):

        # Get Topic for Entry
        top = add_topic()

        # Create Fake Data for entry using faker class (Faker Object)
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # Create new Webpage Entry
        webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]
                # Note: topic is nor fake here, as we selected that one initially

        # Create Fake Access Record for that page
        # Could add more of these if you wanted...
        accRec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

#--------------------------------------------------------------
# Population process:

if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(20)
    print('Populating Complete')