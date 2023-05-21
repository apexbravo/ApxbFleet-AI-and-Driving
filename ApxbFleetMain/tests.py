from unittest.mock import patch
from django.test import TestCase
from ApxbFleetMain.management.commands.my_task import Command
from ApxbFleetMain.models import Driver, DriverLocation


class TestCommand(TestCase):

    @patch('ApxbFleetMain.management.commands.my_task.life360')
    def test_update_driver_location(self, mock_api):
        # Mock the Life360 API client and the authenticate method
        mock_authenticate = mock_api.return_value.authenticate
        mock_authenticate.return_value = True

        # Set up mock data for the circle and member
        mock_member = {
            'firstName': 'John',
            'loginEmail': 'abelrevelation@gmail.com',
            'location': {
                'latitude': 1.234,
                'longitude': 2.345,
            },
        }
        mock_circle = {
            'id': '123',
            'members': [mock_member],
        }
        mock_get_circles = mock_api.return_value.get_circles
        mock_get_circles.return_value = [mock_circle]
        mock_get_circle = mock_api.return_value.get_circle
        mock_get_circle.return_value = mock_circle

        # Create a driver object for the member
        driver = Driver.objects.create(email=mock_member['loginEmail'])
        driver_location = DriverLocation(
            driver=driver, latitude=mock_member['location']['latitude'], longitude=mock_member['location']['longitude'])
        driver_location.save()

        # Call the update_driver_location method
        command = Command()
        self.assertEqual(DriverLocation.objects.count(), 1)

        # Check that the driver location was saved to the database
        driver_location = DriverLocation.objects.get(driver=driver)
        self.assertEqual(float(driver_location.latitude),
                         mock_member['location']['latitude'])
        self.assertEqual(float(driver_location.longitude),
                         mock_member['location']['longitude'])
