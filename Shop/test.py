# test_authentication.py

from django.test import RequestFactory
from authentication import EmployeeAuthentication
from rest_framework.exceptions import AuthenticationFailed

# Assume you have defined your Employees model in models.py

class Employees:
    @classmethod
    def objects(cls):
        return cls

    @staticmethod
    def get(email):
        # Mocking the Employees.objects.get() method for testing purposes
        if email == 'user@example.com':
            return Employees()
        else:
            raise Employees.DoesNotExist()

# Create a mock request object
factory = RequestFactory()
request = factory.get('/')
request.META['HTTP_AUTHORIZATION'] = 'Token user@example.com'  # Sample token for testing

# Instantiate the authentication class
authentication = EmployeeAuthentication()

try:
    # Attempt authentication with the mocked request
    authenticated_user, _ = authentication.authenticate(request)
    print("Authentication successful for user:", authenticated_user)
except AuthenticationFailed as e:
    # Authentication failed
    print("Authentication failed:", e)
