import requests

BASE = "http://127.0.0.1:5000/"

response = requests.put(BASE + "/api/v1/email", {"to": "user_student@email.com",
                                                  "from": "user_instructor@email.com",
                                                  "subject": "Feedback",
                                                  "content": "Your project Feedback is available at www.google.com"
                                                  })
print(response.json())