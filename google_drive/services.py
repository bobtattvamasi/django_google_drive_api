# google_drive/services.py
from googleapiclient.errors import HttpError
from google.oauth2 import service_account
import os
from googleapiclient.discovery import build
from io import BytesIO
from googleapiclient.http import MediaIoBaseUpload

def create_file_in_google_drive(file_obj):
  """
  Creates a file in Google Drive using the Google Drive API.

  Args:
      file_obj: A File model object containing information about the file.

  Returns:
      A dictionary containing information about the created file, or None on error.
  """

  scopes = ['https://www.googleapis.com/auth/drive']
  credentials = service_account.Credentials.from_service_account_file(
      'creds.json',
      scopes=scopes
  )
  service = build('drive', 'v3', credentials=credentials)

  gbf_folder = "16zohQbg4gwTmgIEoZOU5DVD_-LzFNY5q"

  # Prepare file metadata based on the File model object
  body = {
      'name': file_obj.name,
      'mimeType': 'text/plain',  # Adjust based on file content type
      'parents': [gbf_folder]
  }

  fbody = MediaIoBaseUpload(BytesIO(file_obj.data.encode('utf-8')), mimetype='text/plain', resumable=True)

  # Upload the file content
  try:
      file_upload = service.files().create(
          body=body,
          media_body=fbody
      ).execute()
      print(f"file_upload = {file_upload}")

      return file_upload

  except HttpError as error:
      print(f"An error occurred: {error}")
      return None
