from Google import Service
import os
from dotenv import load_dotenv
from email import errors
from apiclient import errors
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import base64
import time
import mimetypes
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

env_path = Path('.') / 'creds.env'
load_dotenv(dotenv_path=env_path)

SCOPES = ['https://mail.google.com/']
API_VERSION = "v1"
CLIENT_SECRET_FILE = os.environ['GOOGLE_OAUTH_CLIENT_FILE']
API_SERVICE_NAME = "Gmail"

service = Service(CLIENT_SECRET_FILE, API_SERVICE_NAME, API_VERSION, SCOPES)
message = MIMEMultipart()

def send_text(to, subject, text):
    message['to'] = to
    message['subject'] = subject
    try:
        message.attach(MIMEText(text, 'plain'))
        raw_string = base64.urlsafe_b64encode(message.as_bytes()).decode()
        sending_message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
        print("Message sent")
    except errors.HttpError:
        print(f'An error occurred:')
        print(errors)

def send_attachment(to, subject, attachments=[]):
    message['to'] = to
    message['subject'] = subject
    for attachment in attachments:
        try:
            content_type, encoding = mimetypes.guess_type(attachment)
            if content_type is None or encoding is not None:
                content_type = 'application/octet-stream'
            main_type, sub_type = content_type.split('/', 1)
            if main_type == 'text' or main_type == 'text/calendar':
                with open(attachment, "rb") as text_file:
                    msg = MIMEBase("application", "octet stream")
                    msg.set_payload(text_file.read())
            elif main_type == 'image':
                fp = open(attachment, 'rb')
                msg = MIMEImage(fp.read(), _subtype=sub_type)
                fp.close()
            elif main_type == 'audio':
                fp = open(attachment, 'rb')
                msg = MIMEAudio(fp.read(), _subtype=sub_type)
                fp.close()
            else:
                fp = open(attachment, 'rb')
                msg = MIMEBase(main_type,sub_type)
                msg.set_payload(fp.read())
                fp.close()
            filename = os.path.basename(attachment)
            msg.add_header('Content-Disposition', 'attachment', filename=filename)
            message.attach(msg)
        except errors.HttpError:
            print("An error has occurred")
            print(errors)
    raw_string = base64.urlsafe_b64encode(message.as_bytes()).decode()
    service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
    print("Attachment successfully sent!")

    

def get_messages(query=''):
    try:
        response = service.users().messages().list(userId='me', q=query).execute()
        messages = []
        if('messages' in response):
                messages.extend(response['messages'])
        while 'nextPageToken' in response:
            page_token = response['nextPageToken']
            response = service.users().messages().list(
                    userId='me',
                    q=query,
                    pageToken=page_token).execute()
            messages.extend(response['messages'])
        return messages
    except errors.HttpError:
        print("An error has occurred")
        print(errors)

def delete_message(message_id):
    try:
        service.users().messages().delete(userId='me', id=message_id).execute()
        print(f'Message Deleted')
    except errors.HttpError as error:
        print(f'An error has occured', error)

def delete_messages_bulk(message_ids):
    time.sleep(20)
    for counter in range(len(message_ids)):
        delete_message(message_ids[counter]['id'])

