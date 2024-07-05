import requests

url = 'http://127.0.0.1:5000/classify'
files = {'file': open('pic2.jpeg', 'rb')}

try:
    response = requests.post(url, files=files)
    response.raise_for_status()  # Raise an HTTPError for bad responses
    print(response.json)
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
