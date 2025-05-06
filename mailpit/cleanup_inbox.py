import requests

MAILPIT_API = "http://localhost:8125/api/v1/messages"

response = requests.delete(MAILPIT_API)

if response.status_code == 200:
    print("✓ Mailpit inbox cleared successfully.")
else:
    print(f"✗ Failed to clear inbox. Status code: {response.status_code}")
