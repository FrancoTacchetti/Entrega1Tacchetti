from django.test import SimpleTestCase
from django.urls import reverse, resolve

# Create your tests here.
class CreateRouteTestCases(SimpleTestCase):
    # Testcases to check that the creation url are being resolve to the expected route
    def test_create_tenant_route(self):
        url = reverse('tenant-create')
        self.assertEquals(resolve(url).route, 'tenant/new')
    
    def test_create_rentable_place_route(self):
        url = reverse('rentable-place-create')
        self.assertEquals(resolve(url).route, 'place/new')

    def test_create_rentable_car_route(self):
        url = reverse('rentable-car-create')
        self.assertEquals(resolve(url).route, 'car/new')

