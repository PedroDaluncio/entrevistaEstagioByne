import logging
from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

API_HOST = os.environ.get("API_HOST")
API_PORT = os.environ.get("API_PORT")

def main():
    """Main function to get data from an web server"""
    user = {"user": "Pedro Henrique Archer Dalsenter"}
    headers = {'content-type': 'application/json'}
    try:
        response = requests.get(f"{API_HOST}:{API_PORT}/get_text", timeout=10)
        print(response.json())
    except Exception:
        logging.exception("Error fething text data")

    try:
        response = requests.post(f"{API_HOST}:{API_PORT}/post_odd_number", data=json.dumps(
            user), timeout=60, headers=headers)
        print(response.json())
    except Exception:
        logging.exception("Error fething text data")

    try:
        response = requests.post(f"{API_HOST}:{API_PORT}/post_even_number", data=json.dumps(
            user), timeout=60, headers=headers)
        print(response.json())
    except Exception:
        logging.exception("Error fething text data")

    try:
        response = requests.get(f"{API_HOST}:{API_PORT}/get_my_last_number?user={user['user']}", timeout=60)
        print(response.json())
    except Exception:
        logging.exception("Error fething text data")


if __name__ == "__main__":
    main()
