from django.test import TestCase


class HomeTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/')  # client Realizar requicoes

    def test_get(self):
        """Get / must return status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Must use index.html"""
        self.assertTemplateUsed(self.resp, 'index.html')

    def test_subscription_link(self):
        self.assertContains(self.resp, 'href="/inscricao/"')