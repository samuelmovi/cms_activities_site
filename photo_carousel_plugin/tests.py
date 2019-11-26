from django.test import TestCase
from .models import CarouselPhoto

# Create your tests here.


class CarouselPhotoTestCase(TestCase):
    test_fields = {
        'name': 'test name',
        'image': 'test image',
    }

    def setUp(self):
        CarouselPhoto.objects.create(
            name=self.test_fields['name'],
            image=self.test_fields['image'],
        )

    def test_content(self):
        photo = CarouselPhoto.objects.get(name=self.test_fields['name'])
        for field in self.test_fields:
            # print("[#] Field: {}".format(field))
            # print("\t> Instance: {}".format(location.__dict__[field]))
            # print("\t> Test value: {}".format(self.test_fields[field]))
            self.assertEqual(photo.__dict__[field], self.test_fields[field])

