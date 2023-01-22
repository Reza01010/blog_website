from idlelib.rpc import response_queue

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post
from django.shortcuts import reverse


class BlogPostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='Reza')
        cls.post1 = Post.objects.create(
            title='post111',
            text='Lorem ipsum',
            status=Post.STATUS_CHOICES[0][0],
            author=cls.user,
        )
        cls.post2 = Post.objects.create(
            title='post2',
            text='Sed vocibus albucius',
            status='drf',
            author=cls.user,
        )

    def test_post_model_str(self):
        post = self.post2
        post1 = self.post1
        self.assertEqual(str(post), post.title)
        self.assertEqual(post1.title, 'post111')
        self.assertEqual(post1.text, 'Lorem ipsum')

    def test_post_list_url(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_post_list_url_by_name(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)

    def test_post_title_on_blog_detail_page(self):
        response = self.client.get(reverse('post_list'))
        self.assertContains(response, self.post1.title)

    def test_post_detail_url(self):
        response = self.client.get(f'/blog/{self.post1.id}/')
        self.assertEqual(response.status_code, 200)

    def test_post_detail_url_name(self):
        response = self.client.get(reverse('post_detail', args=[self.post1.id]))
        self.assertEqual(response.status_code, 200)

    def test_post_details_on_blog_detail_page(self):
        response = self.client.get(f'/blog/{self.post1.id}/')

        print(f'\n---\n-{response, self.post1.text}\n-\n---')
        self.assertContains(response, self.post1.text)
        self.assertContains(response, self.post1.title)
        self.assertIn(self.post1.title, self.post1.title)

    def test_post_template1(self):
        response = self.client.get('/blog/')
        self.assertTemplateUsed(response, 'blog/posts_list.html')

    def test_draft_post_not_show_in_posts_list(self):
        response = self.client.get(reverse('post_list'))
        self.assertContains(response,self.post1.title)
        self.assertNotContains(response,self.post2.title)

    def test_post_add_view(self):
        response = self.client.post(reverse('post_add'), {
            'title': 'Some Title Test',
            'text': 'This is Text',
            'status': 'pub',
            'author': self.user.id,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, 'Some Title Test')
        self.assertEqual(Post.objects.last().text, 'This is Text')
        self.assertEqual(Post.objects.last().status, 'pub')
        self.assertIn(str(Post.objects.last().author), 'Reza') # str('<User: Reza>') =  'Reza' ,,, 'Reza' = 'Reza'




        response_update = self.client.post(reverse('post_update', args=[3]), {
            'title': 'post111111 Title Test',
            'text': 'Lorem ipsum is Text',
            'status': 'drf',
            'author': self.user.id,
        })
        self.assertEqual(response_update.status_code, 302)
        self.assertEqual(Post.objects.last().title, 'post111111 Title Test')
        self.assertEqual(Post.objects.last().text, 'Lorem ipsum is Text')
        self.assertNotEqual(Post.objects.last().status, 'pub')


        response_ceck_list = self.client.get(reverse('post_list'))
        self.assertNotContains(response_ceck_list, 'Lorem ipsum is Text')

    def test_post_delete_view(self):
        response = self.client.post(reverse('post_delete', args=[self.post1.id],))
        self.assertEqual(response.status_code, 302)






















# from django.test import TestCase
# from django.contrib.auth.models import User
# from .models import Post
# from django.shortcuts import reverse
#
#
# class BlogPostTest(TestCase):
#     def setUp(self):
#         self.user = User.objects.create(username='78780780870')
#         self.post1 = Post.objects.create(
#             title='07807878078078',
#             text='0870780780780780780',
#             status=Post.STATUS_CHOICES[0],
#             author=self.user,
#         )
#
#     # def test_post_list_url(self):
#     #     response = self.client.get('/blog/')
#     #     self.assertEqual(response.status_code, 200)
#     #
#     # def test_post_list_url_by_name(self):
#     #     response = self.client.get(reverse('post_list'))
#     #     self.assertEqual(response.status_code, 200)
#
#     def test_post_title_on_blog_detail_page(self):
#         response = self.client.get('/blog')
#         self.assertContains(response, self.post1.title)
#     #
#     # def test_post_detail_url(self):
#     #     response = self.client.get(f'/blog/{self.post1.id}/')
#     #     self.assertEqual(response.status_code, 200)
#     #
#     # def test_post_detail_url_name(self):
#     #     response = self.client.get(reverse('post_detail', args=[self.post1.id]))
#     #     self.assertEqual(response.status_code, 200)
#
#     def test_post_details_on_blog_detail_page(self):
#         response = self.client.get(f'/blog/{self.post1.id}')
#         self.assertContains(response, self.post1.title)
#         self.assertContains(response, self.post1.text)
#

#
#
