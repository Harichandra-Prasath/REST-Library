from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Book
from django.urls import reverse
import json

class BookTestCase(TestCase):

    def setUp(self) -> None:
        book = Book(
            Title="Test",
            Author="Tester",
            ISBN="1234567890123"
        )
        book.save()

    def test_list_books(self):
        _response = self.client.get(reverse('listandcreate'))

        expected_response = [{
            "ISBN":"1234567890123",
            "Title":"Test",
            "Author":"Tester",
            "Publication_Date":None,
            "Description":None
        }]

        self.assertEqual(_response.status_code,200)
        self.assertEqual(json.loads(_response.content),expected_response)

    def test_create_book(self):
        
        post_data = {
            "ISBN":"1234123412341",
            "Title":"Test1",
            "Author":"Tester",
        }

        _response = self.client.post(reverse('listandcreate'),post_data,content_type="application/json")
        self.assertEqual(_response.status_code,201)

    def test_retrieve_book(self):
        _response = self.client.get(reverse('retrieveupdatedelete',kwargs={'isbn':"1234567890123"}))

        expected_response = {
            "ISBN":"1234567890123",
            "Title":"Test",
            "Author":"Tester",
            "Publication_Date":None,
            "Description":None
        }
        
        self.assertEqual(_response.status_code,200)
        self.assertEqual(json.loads(_response.content),expected_response)
    
    def test_update_book(self):
        put_data = {
            "ISBN":"1212121212121",
            "Title":"Updated_Test",
            "Author":"Updated_Tester",
        }
        _response = self.client.put(reverse('retrieveupdatedelete',kwargs={'isbn':"1234567890123"}),data=put_data,content_type="application/json")
        

        expected_response = {
            "ISBN":"1212121212121",
            "Title":"Updated_Test",
            "Author":"Updated_Tester",
            "Publication_Date":None,
            "Description":None
        }
        self.assertEqual(_response.status_code,201)
        self.assertEqual(json.loads(_response.content),expected_response)

    
    def test_delete_book(self):
        _response = self.client.delete(reverse('retrieveupdatedelete',kwargs={'isbn':'1234567890123'}))
        self.assertEqual(_response.status_code,204)
        self.assertEqual(Book.objects.count(),0)


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