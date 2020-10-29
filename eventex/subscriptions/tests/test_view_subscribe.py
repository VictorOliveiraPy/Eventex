from django.core import mail
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscribeGet(TestCase):
    def setUp(self):
        self.resp = self.client.get('/inscricao/')

    def test_get(self):
        """Get /inscricao/ must return status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Must use subscriptions/subscription_form.html"""
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

    def test_html(self):
        """HTML must contain input tags"""
        tags = (('<form', 1),
                ('<input',6),
                ('type="text"',3),
                ('type="email"',1),
                ('type="submit"',1)

        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)

    def test_csrf(self):
        """Html must contain csrf"""
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """Context must have subscription form"""
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    


class SubscribePostValid(TestCase):  # Submisão do form
    def setUp(self):
        data = dict(name='Victor Hugo', cpf='12345678901', email='victor-hugopy@outlook.com',
                    phone='81-998832982')
        self.resp = self.client.post('/inscricao/', data)

    def test_post(self):
        """Valid POST should redirect to /inscricao/"""
        self.assertEqual(302, self.resp.status_code)

    def test_send_subscribe_email(self):   # mail enviando
        self.assertEqual(1, len(mail.outbox))


class SubscribePostInvalid(TestCase):
    def setUp(self):
        self.resp = self.client.post('/inscricao/', {})  # Dados vazio, mostrar os erros

    def test_post(self):
        """Invalid Post should not redirect"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_form_has_erros(self):
        form = self.resp.context['form']


class SubscribeSuccessMessage(TestCase):
    def setUp(self):
        data = dict(name='Victor Hugo', cpf='12345678901',
                    email='victor-hugopy@outlook.com', phone='81-998832982')
        self.resp = self.client.post('/inscricao/', data, follow=True)

    def test_message(self):
        self.assertContains(self.resp, 'Inscrição realizada com sucesso!')


