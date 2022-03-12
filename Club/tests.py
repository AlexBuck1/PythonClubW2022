from django.test import TestCase
from django.contrib.auth.models import User
from .models import Meeting, MeetingMinutes, Event, Resource
from .forms import ResourceForm, MeetingForm
from django.urls import reverse_lazy, reverse

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

class NewResourceForm(TestCase):
    def test_resourceform(self):
        form=ResourceForm(data={
            'resourcename':'Microphone',
            'resourcetype':'Audio',
            'resourceURL':'',
            'resourcedataentered':'2022-03-02',
            'userID':'alexbuck1'
        })
        self.assertTrue(form.is_valid)

class NewMeetingForm(TestCase):
    def test_meetingform(self):
        form=MeetingForm(data={
            'meetingtitle':'March Meeting',
            'meetingdate':'2022-03-02',
            'meetingtime':'12:00:00',
            'meetinglocation':'Gym',
            'meetingagenda':'Monthly recap'
        })
        self.assertTrue(form.is_valid)

class New_Meeting_Authentication_Test(TestCase):
    def setUP(self):
        self.test_user=User.onjects.create_user(username='userOne', password='Jjettas18')
        self.meeting=Meeting.objects.create(meetingtitle='March Meeting', meetingdate='2022-03-02', meetingtime='12:00:00', meetinglocation='Gym', meetingagenda='Monthly recap')

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newmeeting'))
        self.assertRedirects(response, '/accounts/login/?next-/Club/newmeeting/')