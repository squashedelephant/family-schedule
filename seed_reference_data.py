#!/usr/bin/env python3

import os


from django.core.wsgi import get_wsgi_application
os.environ['DJANGO_SETTINGS_MODULE'] = 'family.settings'
application = get_wsgi_application()

from schedule.models import Activity, Child, Color, Event, Parent, WeekDay

def seed_activities():
    activities = ['snuggle', 'walk', 'shopping', 'visit park',
                  'play at Gymboree', 'change diaper', 'read a story',
                  'music lesson', 'run errands with parents', 'lunch',
                  'play alone', 'library story time', 'crawl', 'dinner',
                  'visit petting zoo', 'play', "visit Mommy's friend",
                  'visit Grandparents', 'shopping with Mommy', 'dance',
                  'bath time', 'nursing', 'breakfast', 'change clothes',
                  'sleep in nursery', 'swimming lessons', 'snack', 'car nap']

    for activity in activities:
        a = Activity(name=activity)
        a.save()
    print('seeded Activities')
    return

def seed_colors():
    colors = ['darksalmon', 'yellow', 'gold', 'red', 'royalblue', 'green',
              'skyblue', 'springgreen', 'lightorange', 'orange', 'cyan', 
              'cream', 'blue', 'limegreen', 'brown', 'tan', 'silver', 'white',
              'lightblue', 'olive', 'beige', 'bluegray', 'gray', 'magenta', 
              'lightgreen', 'pink']

    for color in colors:
        c = Color(name=color)
        c.save()
    print('seeded Colors')
    return

def seed_weekdays():
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
                'Saturday', 'Sunday']

    for day in weekdays:
        wd = WeekDay(name=day)
        wd.save()
    print('seeded WeekDays')
    return

def seed_parents():
    parents = [{'first_name': 'Tim',
                'last_name': 'Stilwell'},
               {'first_name': 'Micah',
                'last_name': 'Stilwell'}]
  
    for parent in parents:
        p = Parent(first_name=parent['first_name'],
                   last_name=parent['last_name'])
        p.save()
    print('seeded Parents')
    return

def seed_children():
    children = [{'first_name': 'Meko',
                 'last_name': 'Stilwell',
                 'parents': ['Tim Stilwell', 'Micah Stilwell']},
                {'first_name': 'Ethan',
                 'last_name': 'Stilwell',
                 'parents': ['Tim Stilwell', 'Micah Stilwell']}]
  
    for child in children:
        for parent in child['parents']:
            c = Child(first_name=child['first_name'],
                  last_name=child['last_name'])
            c.save()
            p = Parent.objects.get(first_name=parent.split()[0],
                                   last_name=parent.split()[1])
            if p:
                c.parents.add(p)
    print('seeded Children')
    return

if __name__ == '__main__':
    seed_activities()
    seed_colors()
    seed_weekdays()
    seed_parents()
    seed_children()
