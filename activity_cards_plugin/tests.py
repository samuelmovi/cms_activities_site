from django.test import TestCase
from .models import ActivityCard

# Create your tests here.


class ActivityCardTestCase(TestCase):
    test_fields = {
        'name': 'test name',
        'title': ' test title',
        'text': 'test text',
        'image': 'test image',
        'link': 'test link'
    }

    def setUp(self):
        ActivityCard.objects.create(
            name=self.test_fields['name'],
            title=self.test_fields['title'],
            text=self.test_fields['text'],
            image=self.test_fields['image'],
            link=self.test_fields['link'],
        )

    def test_content(self):
        card = ActivityCard.objects.get(name=self.test_fields['name'])
        for field in self.test_fields:
            # print("[#] Field: {}".format(field))
            # print("\t> Instance: {}".format(location.__dict__[field]))
            # print("\t> Test value: {}".format(self.test_fields[field]))
            self.assertEqual(card.__dict__[field], self.test_fields[field])
