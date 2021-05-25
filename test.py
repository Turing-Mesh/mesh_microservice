import requests

BASE = "http://127.0.0.1:5000/"

response = requests.put(BASE + "/api/v1/email", {"to": "turingmeshtest@gmail.com",
                                                  "from": "turingmesh@email.com",
                                                  "subject": "Feedback",
                                                  "content": "Your project Feedback is available at www.google.com"
                                                  })
print(response.json())