import requests

# references: https://www.w3schools.com/python/ref_requests_post.asp
# references: https://docs.python-requests.org/en/v2.0.0/

MICROSERVICE_URL = "http://localhost:5000/send-email"

test = { # test JSON
  "email": "test_email@gmail.com",
  "message": "test email"
}

response = requests.post(MICROSERVICE_URL, json=test)

if response.status_code == 200: # success
  print(response.json())
else: # some error - 400/500/etc.
  print(response.json())