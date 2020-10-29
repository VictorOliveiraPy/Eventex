from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):  # Submisão do form
    def setUp(self):
        data = dict(name='Victor Hugo', cpf='12345678901', email='victor-hugopy@outlook.com',
                    phone='81-998832982')
        self.resp = self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]  # Lista de e-mail enviados!

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'victor-hugopy@outlook.com'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['victor-hugopy@outlook.com', 'victor-hugopy@outlook.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = ['victor',
                    '12345678901',
                    'victor-hugopy@outlook.com',
                    '81-998832982'

                    ]  # Lista

        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
