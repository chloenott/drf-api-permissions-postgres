from django.test import TestCase
from django.test import Client
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user, get_user_model
from .models import Note
from django.urls import reverse

# Create your tests here.
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
        self.assertEqual(str(note.headline), 'Headline test')


class NoteAPITests(APITestCase):

    def test_list_without_authentication(self):
        response = self.client.get(reverse('list_view'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    def test_list_with_authentication(self):

        test_user = get_user_model().objects.create_user(username='chloe', email='chloe@nott.email', password='pass')
        test_user.save()

        client = Client()
        client.login(username='chloe', email='chloe@nott.email', password='pass')

        response = client.get(path=reverse('list_view'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # # Todo: this doesn't work yet. Responds with 405.
    # def test_put_with_authorization(self):

    #     test_user = get_user_model().objects.create_user(username='chloe', email='chloe@nott.email', password='pass')
    #     test_user.save()

    #     client = Client()
    #     client.login(username='chloe', email='chloe@nott.email', password='pass')

    #     response = client.put(
    #         path=reverse('list_view'), 
    #         data={
    #             'headline': 'Headline test3',
    #             'details': 'Details test',
    #             'user': test_user,
    #         },
    #     )

    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
