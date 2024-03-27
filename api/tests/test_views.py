from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
import json

class UserTestCase(TestCase):

    def setUp(self):
        test_user = User(username="Tester")
        test_user.set_password("Test123")
        test_user.save()
    
    def test_register_view(self):
        post = {
            "Username":"Test",
            "Password":"Test123",
            "Confirm_Password":"Test123"
        }
        _response = self.client.post(reverse("register"),post,content_type="application/json")
        expected_response = {
            "Status":"Success",
            "Message":"Registered_Successfully"
        }
    
        self.assertEqual(_response.status_code,201)
        self.assertEqual(json.loads(_response.content),expected_response)
    
    def test_login_view(self):
        post =  {
            "Username":"Tester",
            "Password":"Test123"
        }
        _response = self.client.post(reverse("login"),post,content_type="application/json")

        self.assertIsNotNone(_response.cookies.get("jwt"))
        self.assertEqual(_response.status_code,200)