import os.path
from googleapiclient.discovery import build, MediaFileUpload
from google.auth.transport.requests import Request
from Library.GoogAuth import _authentication


def UploadToGDrive(filename):
    """Upload the top 5 cast members into a Google Spreadsheet
    """
    service = build('drive', 'v3', credentials=_authentication())

    # Call the Drive v3 API
    file_metadata = {'name': filename}
    media = MediaFileUpload(filename, mimetype='text/csv')
    file = service.files().create(body=file_metadata,
                                        media_body=media,
                                        fields='id').execute()
    print('File ID: %s' % file.get('id'))
