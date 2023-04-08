import life360
from . import Driver
import schedule
import time


# Set up the Life360 API client
authorization_token = "cFJFcXVnYWJSZXRyZTRFc3RldGhlcnVmcmVQdW1hbUV4dWNyRUh1YzptM2ZydXBSZXRSZXN3ZXJFQ2hBUHJFOTZxYWtFZHI0Vg=="
username = "email@address.com"
password = "super long password"
api = life360(authorization_token=authorization_token,
              username=username, password=password)

# Authenticate with the API
if api.authenticate():
    # Get the driver's Life360 ID
    circles = api.get_circles()
    circle_id = circles[0]['id']
    members = api.get_circle_members(circle_id)
    driver = None
    for member in members:
        try:
            driver = Driver.objects.get(email=member['email'])
        except Driver.DoesNotExist:
            # The driver is not in the database, skip this iteration
            continue

    if not driver:
        print("Driver not found in database")
        exit(1)

    def save_driver_location():
        # Get the driver's current location from Life360
        location = api.get_location(member['id'])

        # Create a new DriverLocation object and save it to the database
        driver_location = Driver(
            driver=driver, latitude=location['latitude'], longitude=location['longitude'])
        driver_location.save()

    # Schedule the function to run every 10 minutes
    schedule.every(10).minutes.do(save_driver_location)

    # Run the scheduled functions indefinitely
    while True:
        schedule.run_pending()
        time.sleep(1)
else:
    print("Error authenticating with Life360 API")
