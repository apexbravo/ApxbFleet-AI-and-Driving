import asyncio
import time
from ApxbFleetMain.models import Driver, DriverLocation
from ApxbFleetMain.life360 import life360
from django.core.management.base import BaseCommand
from asgiref.sync import sync_to_async


class Command(BaseCommand):
    help = 'Runs an async task'

    async def update_driver_location(self):
        # Set up the Life360 API client
        authorization_token = "cFJFcXVnYWJSZXRyZTRFc3RldGhlW1hbUV4dWNyRUh1YzptM2ZydXBSZXRSZXN3ZXJFQ2hBUHJFOTZxYWtFZHI0Vg=="
        username = "abelrevelation@gmail.com"
        password = "Blah123"
        api = life360(authorization_token=authorization_token,
                      username=username, password=password)

        # Authenticate with the API
        if api.authenticate():
            # Get the driver's Life360 ID
            circles = api.get_circles()
            circle_id = circles[0]['id']
            circle = api.get_circle(circle_id)
            driver = None
            for member in circle['members']:
                try:
                    print("Name", member['firstName'])
                    driver = await sync_to_async(Driver.objects.get)(email=member['loginEmail'])
                    break
                except Driver.DoesNotExist:
                    pass

            if not driver:
                print("Driver not found in database")
                return

            # Get the driver's current location from Life360
            location = member['location']

            # Create a new DriverLocation object and save it to the database
            driver_location = DriverLocation(
                driver=driver, latitude=location['latitude'], longitude=location['longitude'])
            await sync_to_async(driver_location.save)()

            print(
                f"Driver location updated: {location['latitude']}, {location['longitude']}")
        else:
            print("Error authenticating with Life360 API")

    async def run_update_task(self):
        while True:
            await self.update_driver_location()
            await asyncio.sleep(5)  # Wait for 60 seconds before running again

    def handle(self, *args, **options):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.run_update_task())
