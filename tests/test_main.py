import unittest
import json
from main import *

class MainTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_successful_email_status(self):
        payload = json.dumps({"to": "test@example.com",
                           "subject": "Test",
                           "content": "This is a test"
                          })

        response = self.app.put('/api/v1/email', headers={"Content-Type": "application/json"}, data=payload)
        self.assertEqual(response.status_code, 200)

    def test_successful_email_content_type(self):
        payload = json.dumps({"to": "test@example.com",
                           "subject": "Test",
                           "content": "This is a test"
                          })
        response = self.app.put('/api/v1/email', headers={"Content-Type": "application/json"}, data=payload)
        self.assertEqual(response.content_type, 'application/json')

    def test_successful_email_data(self):
        payload = json.dumps({"to": "test@example.com",
                           "subject": "Test",
                           "content": "This is a test"
                          })
        response = self.app.put('/api/v1/email', headers={"Content-Type": "application/json"}, data=payload)
        self.assertTrue(b'data' in response.data)
        self.assertEqual(response.data, b'{"data": "Email has been sent successfully"}\n')



    def test_sad_path_to_is_required(self):
        payload = json.dumps({
                           "subject": "Test",
                           "content": "This is a test"
                          })

        response = self.app.put('/api/v1/email', headers={"Content-Type": "application/json"}, data=payload)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.status, '400 BAD REQUEST')
        self.assertEqual(response.data, b'{"message": {"to": "Recipient Email Required"}}\n')

    def test_sad_path_subject_is_required(self):
        payload = json.dumps({
                           "to": "test@example.com",
                           "content": "This is a test"
                          })

        response = self.app.put('/api/v1/email', headers={"Content-Type": "application/json"}, data=payload)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.status, '400 BAD REQUEST')
        self.assertEqual(response.data, b'{"message": {"subject": "Subject Line Required"}}\n')

    def test_sad_path_content_is_required(self):
        payload = json.dumps({
                           "to": "test@example.com",
                           "subject": "Test"
                          })

        response = self.app.put('/api/v1/email', headers={"Content-Type": "application/json"}, data=payload)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.status, '400 BAD REQUEST')
        self.assertEqual(response.data, b'{"message": {"content": "Content Required"}}\n')



