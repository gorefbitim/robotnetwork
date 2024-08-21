"""
Test script for interacting with FastAPI server handling Venus robot messages.

This script sends GET requests to a FastAPI server endpoint `/venusslack`
designed to relay messages from VENUS (Hamilton liquid handling robot language)
to a Slack webhook. The test includes sending a single message and a long
message to simulate different payload sizes.

The test expects the FastAPI server to be running at
`http://localhost:8000/venusslack`.

API Concept:
The FastAPI server receives an HTTP GET request at the `/venusslack` endpoint.
The request contains a message parameter, which is processed and sent to a
Slack channel via a webhook. The server then returns a JSON response indicating
the success or failure of the operation.
"""

import requests

SERVER_URL = "http://localhost:8000/venusslack"  # Matches /venusslack route
TEST_MESSAGE = "Step: carrier unload is done, nice."

# Send GET request to FastAPI server
response = requests.get(SERVER_URL, params={"message": TEST_MESSAGE})

# Check and print the response
if response.status_code == 200:
    print("Success:", response.json())
else:
    print(f"Failed: {response.status_code}, {response.text}")

# Check the length of the message multiplied by 20
print("Trying a long payload (security risk) ... ")
response = requests.get(SERVER_URL, params={"message": TEST_MESSAGE * 20})
print(f"{response.text}")
