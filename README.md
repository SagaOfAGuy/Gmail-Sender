# Google-Services

Python command-line utility for sending Gmail messages through Gmail API.

  

## Installation

Install pipenv if not installed on system, assuming pip3 is installed:

  

```bash
pip3 install pipenv
```

Now that pipenv is installed, navigate to this project's directory, or wherever you've installed it:

  

```bash
cd /path/to/Google-Services
```

Execute the following Pipenv command to install the dependencies needed for this project found within the Pipfile, which is found within the project directory:

```bash
pipenv install
```

If Pipenv isn't installing properly, edit the Pipfile, and change the python version in the Pipfile:
```bash
# Find Python3 version
python3 --version

# Edit this part of the Pipfile to whatever python version you have. 
[requires]
# Set python_version to 3.9 ONLY if you have version 3.9. If you have 3.8 or 3.7 set it to that
python_version = "3.9"
```
## Configuring Credentials for Google-Services

  

Download this project, and navigate to the directory where you downloaded the project:

```bash
cd /path/to/Google-Services
```

  

Next, go into your Google Account, and create a new Google Cloud Project. Within this project, enable the Gmail API, and download the Client JSON file to access the API.

Make sure you navigated to where you saved Google-Services, and save the Client JSON file there.

  

Next, create a file named "creds.env" to store credentials:
```bash
touch creds.env
```

Use your favorite text editor to edit the file you just created:

```bash
nano creds.env
```

Create an environmental variable and set it equal to the name of the Client JSON file you just saved within the creds.env file:

```bash
GOOGLE_OAUTH_CLIENT_FILE="Your_Client_Secret.json"
```

  
  

## Usage

```bash
# If you want to send a simple Gmail message:
python3 SendGmail.py -to "example@gmail.com" -subject "Testing" -message "Testing testing"

# If you want to send a simple Gmail with an attachment:
python3 SendGmailAttachment.py -to "example@gmail.com" -subject "Testing" -attachment "/home/user/test.png"
```

  

## License

[MIT](https://choosealicense.com/licenses/mit/)
