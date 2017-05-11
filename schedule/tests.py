from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from pytz import UTC
from random import randint
from sys import exit
from ujson import dumps, loads

from django.test import Client, TestCase, TransactionTestCase

from schedule.constant import Constant
from schedule.error import Error
from schedule.models import Activity, Child, ChildImage, Color, Event, Parent, ParentImage, WeekDay

class ActivityTestCase(TestCase):
    def setUp(self):
        self.suffix = randint(1000, 50000)
        self.name = 'nap time {}'.format(self.suffix)

    def tearDown(self):
        self.suffix = 0
        self.name = None

    def test_create_get(self):
        expected = Activity(name=self.name)
        expected.save()
        actual = Activity.objects.get(id=expected.id)
        self.assertEqual(expected.id, actual.id)

class ColorTestCase(TestCase):
    def setUp(self):
        self.suffix = randint(1000, 50000)
        self.name = 'blue {}'.format(self.suffix)

    def tearDown(self):
        self.suffix = 0
        self.name = None

    def test_create_get(self):
        expected = Color(name=self.name)
        expected.save()
        actual = Color.objects.get(id=expected.id)
        self.assertEqual(expected.id, actual.id)

class WeekDayTestCase(TestCase):
    def setUp(self):
        self.suffix = randint(1000, 50000)
        self.name = 'Monday {}'.format(self.suffix)

    def tearDown(self):
        self.suffix = 0
        self.name = None

    def test_create_get(self):
        expected = WeekDay(name=self.name)
        expected.save()
        actual = WeekDay.objects.get(id=expected.id)
        self.assertEqual(expected.id, actual.id)

class ParentTestCase(TestCase):
    def setUp(self):
        self.suffix = randint(1000, 50000)
        self.parent_first_name = 'John Q.'
        self.parent_last_name = 'Public {}'.format(self.suffix)

    def tearDown(self):
        self.suffix = 0
        self.parent_first_name = None
        self.parent_last_name = None

    def test_create_get(self):
        expected = Parent(first_name=self.parent_first_name,
                          last_name=self.parent_last_name,
                          deleted=False)
        expected.save()
        actual = Parent.objects.get(id=expected.id)
        self.assertEqual(expected.id, actual.id)

class ParentImageTestCase(TestCase):
    def setUp(self):
        self.suffix = randint(1000, 50000)
        self.parent_first_name = 'John Q.'
        self.parent_last_name = 'Public {}'.format(self.suffix)
        self.name = 'Tim: football'
        self.url = '/static/images/Tim/football.jpg'

    def tearDown(self):
        self.suffix = 0
        self.parent_first_name = None
        self.parent_last_name = None
        self.name = None
        self.url = None

    def test_create_get(self):
        p = Parent(first_name=self.parent_first_name,
                    last_name=self.parent_last_name,
                    deleted=False)
        p.save()
        expected = ParentImage(parent=p,
                               name=self.name,
                               url=self.url,
                               deleted=False)
        expected.save()
        actual = ParentImage.objects.get(id=expected.id)
        self.assertEqual(expected.id, actual.id)

class ChildTestCase(TestCase):
    def setUp(self):
        self.suffix = randint(1000, 50000)
        self.parent_first_name = 'John Q.'
        self.parent_last_name = 'Public {}'.format(self.suffix)
        self.first_name = 'Baby'
        self.last_name = 'New Year {}'.format(self.suffix)

    def tearDown(self):
        self.suffix = 0
        self.parent_first_name = None
        self.parent_last_name = None
        self.first_name = None
        self.last_name = None

    def test_create_get(self):
        p = Parent(first_name=self.parent_first_name,
                    last_name=self.parent_last_name,
                    deleted=False)
        p.save()
        expected = Child(first_name=self.first_name,
                         last_name=self.last_name,
                         deleted=False)
        expected.save()
        expected.parents.add(p)
        actual = Child.objects.get(id=expected.id)
        self.assertEqual(expected.id, actual.id)

class ChildImageTestCase(TestCase):
    def setUp(self):
        self.suffix = randint(1000, 50000)
        self.parent_first_name = 'John Q.'
        self.parent_last_name = 'Public {}'.format(self.suffix)
        self.first_name = 'Baby'
        self.last_name = 'New Year {}'.format(self.suffix)
        self.name = 'Ethan: happy'
        self.url = '/static/images/Ethan/happy.jpg'

    def tearDown(self):
        self.suffix = 0
        self.parent_first_name = None
        self.parent_last_name = None
        self.first_name = None
        self.last_name = None
        self.name = None
        self.url = None

    def test_create_get(self):
        p = Parent(first_name=self.parent_first_name,
                    last_name=self.parent_last_name,
                    deleted=False)
        p.save()
        c = Child(first_name=self.first_name,
                  last_name=self.last_name,
                  deleted=False)
        c.save()
        c.parents.add(p)
        expected = ChildImage(child=c,
                              name=self.name,
                              url=self.url,
                              deleted=False)
        expected.save()
        actual = ChildImage.objects.get(id=expected.id)
        self.assertEqual(expected.id, actual.id)

class EventTestCase(TestCase):
    def setUp(self):
        self.suffix = randint(1000, 50000)
        self.parent_first_name = 'John Q.'
        self.parent_last_name = 'Public {}'.format(self.suffix)
        self.first_name = 'Baby'
        self.last_name = 'New Year {}'.format(self.suffix)
        t = datetime.now()
        self.created = datetime(t.year, t.month, t.day, t.hour, t.minute, t.second, tzinfo=UTC)
        self.name = 'nap time'
        self.color = 'lightblue'
        self.count = 1

    def tearDown(self):
        self.suffix = 0
        self.parent_first_name = None
        self.parent_last_name = None
        self.first_name = None
        self.last_name = None
        self.created = None
        self.name = None
        self.color = None
        self.count = 0

    def test_create_get(self):
        p = Parent(first_name=self.parent_first_name,
                    last_name=self.parent_last_name,
                    deleted=False)
        p.save()
        c = Child(first_name=self.first_name,
                  last_name=self.last_name,
                  deleted=False)
        c.save()
        c.parents.add(p)
        a = Activity(name=self.name)
        a.save()
        color = Color(name=self.color)
        color.save()
        expected = Event(child=c,
                         created=self.created,
                         name=a,
                         color=color,
                         count=self.count,
                         deleted=False)
        expected.save()
        expected.parents.add(p)
        actual = Event.objects.get(id=expected.id)
        self.assertEqual(expected.id, actual.id)

class APITestCase(TransactionTestCase):
    def setUp(self):
        self.c = Client()
        self.suffix = randint(1000, 50000)
        self.parent_first_name = 'John Q.'
        self.parent_last_name = 'Public {}'.format(self.suffix)

    def tearDown(self):
        self.c = None

    def test_get_index(self):
        r = self.c.get(path='/')
        self.assertEqual(200, r.status_code)
        self.assertEqual('OK', r.reason_phrase)
        soup = BeautifulSoup(r.content, 'html.parser')
        self.assertEqual(u'div', soup.find(id='outside').name)
        self.assertEqual(u'div', soup.find(id='inside').name)
        self.assertEqual(u'nav', soup.find(id='menu').name)
        self.assertEqual(u'article', soup.find(id='summary').name)
        self.assertEqual(u'article', soup.find(id='carousel').name)
        self.assertEqual(u'article', soup.find(id='events').name)
        self.assertEqual(Constant.FOOTER, soup.footer.string)
        self.assertEqual(Constant.HEADER, soup.header.string)
        self.assertEqual(Constant.TITLE, soup.title.string)

    def ttest_get_parent_form(self):
        r = self.c.get(path='/parent')
        self.assertEqual(200, r.status_code)
        self.assertEqual('OK', r.reason_phrase)
        soup = BeautifulSoup(r.content, 'html.parser')
        self.assertEqual(u'form', soup.find(id='parent').name)

    def ttest_create_parent(self):
        data = {'first_name': self.parent_first_name,
                'last_name': self.parent_last_name}
        r = self.c.post(path='/family/parent',
                        data=data)
        self.assertEqual(201, r.status_code)
        self.assertEqual('OK', r.reason_phrase)
        self.assertIsInstance(r.json()['id'], int)
