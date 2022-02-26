from django.test import TestCase
from django.contrib.auth.models import User
from .models import Meeting, MeetingMinutes, Event, Resource

# Create your tests here.
class MeetingTest(TestCase):
    def setUp(self):
        self.type=Meeting(meetingtitle='Introduction Meeting')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'Introduction Meeting')

    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class MeetingMinutesTest(TestCase):
    def setUp(self):
        self.type=MeetingMinutes(meetingminutestext='meeting 1')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'meeting 1')

    def test_tablename(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'meetingminutes')
    
class ResourceTest(TestCase):
    def setUp(self):
        self.name=Resource(resourcename= 'Laptop')
    
    def test_typestring(self):
        self.assertEqual(str(self.name), 'Laptop')

    def test_tablename(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')

class EventTest(TestCase):
    def setUP(self):
        self.name=Event(eventitle='Christmas Party')
    
    def test_typestring(self):
        self.assertEqual(str(self.type), 'Christmas Party')
    
    def test_tablename(self):
        self.assertEqual(str(Event._meta.db_table),'event')