import requests
import json

url = "http://localhost:11434/api/generate"
headers = {"Content-Type": "application/json"}

data = {
    "model": "codellama:latest",
    "prompt": "print sum of two numbers in python",
    "stream": False
}

response = requests.post(url, headers=headers, data=json.dumps(data))
print(response.status_code)
print(response.text)
