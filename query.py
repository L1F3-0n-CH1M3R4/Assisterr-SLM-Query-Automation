import requests
import time
import os
from dotenv import load_dotenv

load_dotenv()

# Config
API_KEY = os.getenv("ASSISTERR_API_KEY")  # APIkey
HANDLE_NAME = os.getenv("ASSISTERR_HANDLE_NAME")  # Handle name
API_URL = f"https://api.assisterr.ai/api/v1/slm/{HANDLE_NAME}/chat/" # API URL
QUERY_FILE = "web3_queries.txt"  # File containing yqueries
OUTPUT_FILE = "responses.txt"  # File to save the responses
DELAY_BETWEEN_REQUESTS = 120  # Delay in seconds between requests


# Headers for the API request
headers = {
    "X-Api-Key": API_KEY,
    "Content-Type": "application/json"
}

# Read queries from the file and process them
with open(QUERY_FILE, "r", encoding="utf-8") as query_file, open(OUTPUT_FILE, "w", encoding="utf-8") as response_file:
    for query in query_file:
        query = query.strip()
        if not query:
            continue  # Skip empty lines

        # Prepare the payload
        payload = {"query": query}

        try:
            # Send the POST request to the API
            response = requests.post(API_URL, json=payload, headers=headers)
            response.raise_for_status()  # Raise an error for bad status codes
            response_data = response.json()
            answer = response_data.get("response", "No response received")
        except Exception as e:
            answer = f"Error: {str(e)}"

        # Write the query and its response to the output file
        response_file.write(f"Q: {query}\nA: {answer}\n\n")

        # Wait before sending the next request
        time.sleep(DELAY_BETWEEN_REQUESTS)

print(f"Processing complete! Responses saved to {OUTPUT_FILE}")