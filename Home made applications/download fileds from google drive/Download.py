from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import io
import os
import requests
from googleapiclient.http import MediaIoBaseDownload

# If modifying these SCOPES, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

def authenticate():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'D:/github/Projects/Home made applications/download fileds from google drive/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return creds

def download_files():
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)
    
    # Specify the ID of your folder
    folder_id = "19jM9zjYHARRMYzbYuMwjyC5BxgQpnJwg"
    
    # Specify the destination directory
    destination_directory = "D:/github/Projects/Home made applications/download fileds from google drive"
    
    # Query the files in the specific folder
    query = f"'{folder_id}' in parents"
    results = service.files().list(q=query, pageSize=10).execute()
    items = results.get('files', [])
    
    # Download each file
    for item in items:
        file_id = item['id']
        request = service.files().get_media(fileId=file_id)
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
        
        # Concatenate the destination directory with the file name
        file_path = os.path.join(destination_directory, item['name'])
        with open(file_path, 'wb') as f:
            f.write(fh.getvalue())
        print(f"File {item['name']} downloaded to {file_path}")

if __name__ == '__main__':
    download_files()
