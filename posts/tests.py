from django.test import TestCase
from .models import Post


class PostTestCase(TestCase):
    def setUp(self):
        self.post1 = Post.objects.create(
            title='Статья 1',
            author='Егор',
            redactor='Python developer',
            date_of_creation='2016-05-30 12:58:57.860860',
            date_of_change='2016-05-30 12:58:57.860860',
            contents_of_post='Бла, бла'
        )
        self.post2 = Post.objects.create(
            title='Статья 2',
            author='Ден',
            redactor='Редактор',
            date_of_creation='2016-05-30 12:58:57.860860',
            date_of_change='2016-05-30 12:58:57.860860',
            contents_of_post='Познавательная статья'
        )

    def tearDown(self):
        self.post1.delete()
        self.post2.delete()

    def test_logged_user_get_homepage(self):
        response = self.client.get('/', follow=True)
        self.assertEqual(response.status_code, 200)


