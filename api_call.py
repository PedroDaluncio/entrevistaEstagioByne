import logging
from dotenv import load_dotenv
import os
import requests

load_dotenv()

API_HOST = os.environ.get("API_HOST")
API_PORT = os.environ.get("API_PORT")

def main():
    """Main function to get data from an web server"""
    try:
        response = requests.get(f"{API_HOST}:{API_PORT}/get_text")
        print(response.json())
    except Exception:
        logging.exception("Error fething text data")

    try:
        response = requests.get(f"{API_HOST}:{API_PORT}/get_odd_number")
        print(response.json())
    except Exception:
        logging.exception("Error fething text data")

    try:
        response = requests.get(f"{API_HOST}:{API_PORT}/get_even_number")
        print(response.json())
    except Exception:
        logging.exception("Error fething text data")


if __name__ == "__main__":
    main()