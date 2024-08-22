# Robotnetwork

A FastAPI server that relays HTTP requests from VENUS (Hamilton robot language)
to Slack via webhooks for streamlined robot notifications.

## Project Overview

This project focuses on establishing seamless communication between robotic
systems (specifically VENUS-enabled Hamilton robots) and Slack, providing
real-time notifications through webhooks. This enables efficient monitoring
and immediate response capabilities directly within Slack channels.

## Advantages of Using a Relay Server

Although it is theoretically possible to directly use HTTPS from VENUS to
communicate with Slack, employing a relay server like the one provided in
this project offers several advantages:

- **Flexibility**: The relay server can easily adapt to various data formats
  and communication protocols, making it simpler to integrate and manage
  different types of messages or data that need to be sent to Slack.
- **Protocol Compatibility**: In scenarios where direct HTTPS communication
  from VENUS does not meet the specific protocols required by Slack, the relay
  server acts as an intermediary, ensuring that messages are formatted and
  transmitted correctly according to Slack's specifications.
- **Enhanced Security**: Using a relay server allows for additional layers
  of security checks and data validation before messages are forwarded to Slack,
  reducing the risk of leaking proprietary data by the scientist.

These benefits make the relay approach more robust and versatile for real-time
communication between robotic systems and Slack channels.


## Features

- **Hamilton VENUS Example**: Utilizes the official Hamilton HTTP
  library to send text to the relay server.
- **FastAPI Server**: Manages HTTP requests from the VENUS robot system
  to relay messages effectively.
- **Slack Integration**: Posts status updates or alerts directly to a
  configured Slack channel via webhooks.
- **Easy Configuration**: Leverages environment variables for Slack webhook
  URLs and other settings to simplify setup and adjustments.


## Prerequisites
To run this application, you will need the following:

- **Hamilton VENUS**: Ensure you have access to the Hamilton VENUS software or
  ystem.
- **Python 3.x**: A compatible version of Python.
- **pip**: Python's package installer, required for managing external
  libraries.
- **Virtualenv**: Optional but recommended for creating isolated Python
  environments. This ensures that dependencies required by the project
  do not interfere with those of other Python projects on the same system.

## Installation

### 1. Install the Package
To install the current release of the package, use pip:

```pip install robotnetwork```

### 2. Setup Slack web-hook

This section guides you through configuring a Slack webhook to receive
notifications from your VENUS application based on any logic you implement.
Follow these steps to create and set up a Slack app that can send notifications
directly to your chosen Slack channel.

2.1. **Create a Slack App:**
   - Go to the [Slack API](https://api.slack.com/apps) page and click on
     "Create New App" (ensure you are signed in).
   - Choose "From scratch," name your app, and select the Slack workspace
     where you want to send notifications.
   - Click "Create App."

2.2. **Configure Incoming Webhooks:**
   - In your app settings, navigate to "Incoming Webhooks" from the sidebar.
   - Enable the feature by toggling the activation switch to "On."
   - Click "Add New Webhook to Workspace" and choose the Slack channel
     where you wish to receive notifications.
   - Slack will generate a Webhook URL; copy this URL as it will be used during
     setup, so that the server can send notifications from your application.

### 3. Run the Server
Run the FastAPI server using this command:

```robotnetwork```

### 4. Initial Setup
During the first run, you will be prompted to input the Slack webhook URL:

**"Enter your Slack webhook URL: "**

Upon entering the URL, it will be securely saved in your home directory,
ensuring it's not exposed or hardcoded in your application code.

#### Note: Where is the URL saved?
- Unix Systems: The URL is stored in the home directory identified by the HOME
environment variable. If HOME is not set, the home directory is determined
using the system's password directory.

- Windows Systems: The URL is saved in the directory specified by USERPROFILE.
If USERPROFILE is not set, it combines HOMEPATH and HOMEDRIVE to determine the
correct location.

This setup provides a secure and convenient way to store sensitive
configuration data, making it easily accessible for your application
while maintaining good security practices.

### 5. Setup VENUS method to send http requests to the server
5.1  Install HSLHttp
Before you can add Slack notifications to your VENUS methods, you need to
install the HSLHttp tool. This installation is crucial for enabling HTTP
requests from within VENUS scripts.

On your VENUS (Windows) computer:
```run_installer.bat```

Safe and Verified Source: The HSLHttp tool is developed and distributed by
Hamilton, ensuring that it is safe and reliable. This can be verified through
the included installer and documentation files within the 'HSLHttp' directory
in our repository.

5.2: Incorporate HTTP Requests in Your Method
Once HSLHttp is installed, you can add HTTP request capabilities to your VENUS
methods to send notifications to the server.

Modify Your VENUS Method: Integrate HTTP request sections into your VENUS method
scripts. Use the provided aliquotes_1_3_slack.hsl file as a template for how to
structure these requests within your method.

## Conclusion
By automating or guiding the installation of necessary tools and integrating
HTTP functionality into your VENUS methods, you can enhance the automation
capabilities of your lab setups, ensuring effective communication via Slack
notifications.

