from django.test import RequestFactory, TestCase
from .views import get_hotels
from .models import City, Hotel
from .views import select_city


class SelectCityViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.city = City.objects.create(cityCode='TEST', name='Test City')

    def test_select_city_view(self):
        request = self.factory.get('/select_city/')
        response = select_city(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test City')


class GetHotelsViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.city = City.objects.create(cityCode='TEST', name='Test City')
        self.hotel = Hotel.objects.create(city=self.city, cityCode='TEST', hotelNr='TEST01', name='Test Hotel')

    def test_get_hotels_view(self):
        request = self.factory.get('/get_hotels/', {'city_id': self.city.id})
        response = get_hotels(request)
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(str(response.content, encoding='utf8'), {'hotels': [{'id': self.hotel.id, 'city_id': self.city.id, 'cityCode': 'TEST', 'hotelNr': 'TEST01', 'name': 'Test Hotel'}]})
