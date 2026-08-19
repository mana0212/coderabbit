import requests

def get_user_details():
  response = requests.get("https://api.example.com/user")
  return response.json()
