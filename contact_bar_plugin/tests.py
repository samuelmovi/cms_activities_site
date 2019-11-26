from django.test import TestCase
from .models import Contact

# Create your tests here.


class ContactTestCase(TestCase):
    test_fields = {
        'name': 'test name',
        'link': 'test link',
        'text': 'test text',
        'icon': 'test icon',
    }

    def setUp(self):
        Contact.objects.create(
            name=self.test_fields['name'],
            link=self.test_fields['link'],
            text=self.test_fields['text'],
            icon=self.test_fields['icon'],
        )

    def test_content(self):
        contact = Contact.objects.get(name=self.test_fields['name'])
        for field in self.test_fields:
            # print("[#] Field: {}".format(field))
            # print("\t> Instance: {}".format(location.__dict__[field]))
            # print("\t> Test value: {}".format(self.test_fields[field]))
            self.assertEqual(contact.__dict__[field], self.test_fields[field])

