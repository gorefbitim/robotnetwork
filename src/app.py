import os
import configparser
from fastapi import FastAPI, Query, HTTPException
import requests
import uvicorn


# Constants
HOME_DIR = os.path.expanduser("~")  # Gets the user's home directory
CONFIG_DIR = os.path.join(HOME_DIR, ".robotnetwork")  # Config directory path
CONFIG_FILE_PATH = os.path.join(CONFIG_DIR, "webhook.txt")  # Full path
SECURITY_STRING_LENGTH_MAX = 256


# Function to load or create configuration
def load_or_create_config():
    # Ensure the configuration directory exists
    os.makedirs(CONFIG_DIR, exist_ok=True)
    config = configparser.ConfigParser()
    if not os.path.exists(CONFIG_FILE_PATH):
        # Ask for the Slack webhook URL if not configured
        webhook_url = input("Enter your Slack webhook URL: ")
        config['DEFAULT'] = {'SLACK_WEBHOOK_URL': webhook_url}
        with open(CONFIG_FILE_PATH, 'w') as configfile:
            config.write(configfile)
    else:
        config.read(CONFIG_FILE_PATH)
    return config


# Load or create the configuration
config = load_or_create_config()


app = FastAPI()


# Retrieve the Slack webhook URL
SLACK_WEBHOOK_URL = config['DEFAULT'].get('SLACK_WEBHOOK_URL')


@app.get("/venusslack")  # Ensure the path is correct
async def stuck_notification(
        message: str = Query(default="We are stuck. Need assistance!")):
    """Tell Slack we are stuck with a custom message."""
    if len(message) > SECURITY_STRING_LENGTH_MAX:
        return {"message": "message too long"}

    response = requests.post(SLACK_WEBHOOK_URL, json={"text": message})
    # Check if Slack webhook was successful
    if response.status_code == 200:
        return {"message": f"Slack notified with message: '{message}'"}
    else:
        raise HTTPException(status_code=500, detail="Failed to notify Slack.")


def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
