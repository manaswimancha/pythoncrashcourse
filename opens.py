import os
from sendgrid import SendGridAPIClient


sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))

params = {'query': 'from_email="email@example.com"', 'limit': 10}

response = sg.client.messages.get(
    query_params=params
)

print(response.status_code)
print(response.body)
print(response.headers)