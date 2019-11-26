from django.test import TestCase
from .models import TextModel
# Create your tests here.


class TextModelTestCase(TestCase):
    test_fields = {
        'title': 'test title',
        'content': 'test content',
    }

    def setUp(self):
        TextModel.objects.create(
            title=self.test_fields['title'],
            content=self.test_fields['content'],
        )

    def test_content(self):
        model = TextModel.objects.get(title=self.test_fields['title'])
        for field in self.test_fields:
            # print("[#] Field: {}".format(field))
            # print("\t> Instance: {}".format(location.__dict__[field]))
            # print("\t> Test value: {}".format(self.test_fields[field]))
            self.assertEqual(model.__dict__[field], self.test_fields[field])

