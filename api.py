from typing import *
import requests
import json

def get_response(prompt: str, model_name: Optional[str] = 'llama3.3:70b') -> str:
        # Example implementation for sending a request to the API
        url = f"http://localhost:11434/api/chat"
        payload = {
            "model": model_name, 
            "stream":False,
            "messages": [{"role": "user", "content": prompt}]
        }
        response = requests.post(url, json=payload)
        text= response.json()['message']['content']
        return text if response.status_code == 200 else "Error: Unable to fetch response"

get_response("Hello, how are you?", "llama3.3:70b")