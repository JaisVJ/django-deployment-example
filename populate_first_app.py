import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'UdemyProject.settings')

import django
django.setup()

import random
from AppTwo.models import AccessRecord, Webpage, Topic
from faker import Faker


fake = Faker()
topics = ['Search', 'Social', 'MarketPlace', 'News', 'Games']


def add_topics():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(n=5):
    for entry in range(n):
        top = add_topics()

        fake_url = fake.url()
        fake_date = fake.date()
        fake_name = fake.company()

        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]
        webpg.save()
        acc_rec.save()


if __name__ == '__main__':
    populate(20)
    print('complete')



