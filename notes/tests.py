from django.test import TestCase, TransactionTestCase
from django.test import Client
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APITransactionTestCase
from rest_framework import status
from django.contrib.auth import get_user, get_user_model
from .models import Note
from django.urls import reverse

#things to check
# transactiontestcase. does apitestcase have an analogue? is there also a functional difference between testcase and transacttestcast (does the reset happen between classes or after all testing is complete)
# can classes be inside other classes and if so how?
# try out teardownclass
class NoteModelTests(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:

        testuser = get_user_model().objects.create_user(
            username='chloe',
            email='chloe@nott.email',
            password='pass'
        )
        testuser.save()

        test_note = Note.objects.create(
            headline = 'Headline test',
            details = 'Details test',
            user = testuser
        )
        test_note.save()


    def test_note_object(self):
        note = Note.objects.get(id=1)
        print(note)
        self.assertEqual(str(note.headline), 'Headline test')


class NoteAPITests(APITransactionTestCase):

    def test_list_without_authentication(self):
        response = self.client.get(reverse('list_view'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    def test_list_with_authentication(self):

        test_user = get_user_model().objects.create_user(username='testing_user', email='testing_user@nott.email', password='pass')
        test_user.save()

        self.client.login(username='testing_user', email='testing_user@nott.email', password='pass')

        response = self.client.get(path=reverse('list_view'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Todo: This affects test_note_object; when enabled there is nothing with id=1 in test_note_object nor test_note_with_authorization. 
    def test_note_with_authorization(self):

        test_user = get_user_model().objects.create_user(username='testing_user', email='testing_user@nott.email', password='pass')
        test_user.save()
        self.client.login(username='testing_user', email='testing_user@nott.email', password='pass')

        response = self.client.post(
            path=reverse('list_view'), 
            data={
                'headline': 'Headline test4',
                'details': 'Details test',
                'user': test_user.pk
            }
        )
        #self.assertEqual(str(Note.objects.get()), 'Headline test2')  # Shows that the post went to id=2. Also, get(id=1) shows nothing exists at 1.
        self.assertEqual(response.content, status.HTTP_201_CREATED)
