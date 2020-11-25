from django.core.exceptions import ValidationError
from django.test import TestCase

from eventex.core.models import Speaker, Contact


class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Victor Hugo',
            slug='victor-hugo',
            photo='http://hbn.link/hb-pic'

        )

    def test_email(self):
        contact = Contact.objects.create(speaker=self.speaker, kind='E',
                                         value='henrique@bastos.net'
                                         )

    def test_phone(self):
        contact = Contact.objects.create(speaker=self.speaker, kind='Contact.EMAIL',
                                         value='81-998832982'
                                         )

        self.assertTrue(Contact.objects.exists())

    def test_choices(self):
        """Contact kind sould be Limited to E or P"""
        contact = Contact(speaker=self.speaker, kind='A', value='Contact.PHONE')
        self.assertRaises(ValidationError, contact.full_clean)

    def test_str(self):
        contact = Contact(speaker=self.speaker, kind='Contact.EMAIL',
                          value='henrique@bastos.net'
                          )
        self.assertEqual('henrique@bastos.net', str(contact))
