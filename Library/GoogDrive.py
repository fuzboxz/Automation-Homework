import os.path
from googleapiclient.discovery import build, MediaFileUpload
from Library.GoogAuth import _authentication


def UploadToGDrive(filename):
    """Upload the top 5 cast members into a Google Spreadsheet and return id of the uploaded file
    """
    service = build('drive', 'v3', credentials=_authentication())

    # Delete earlier revisions
    _deleteEarlier(service, 'top5')
    
    # Upload file and return file id
    file_id = _uploadFile(service, filename)
    return file_id

def _deleteEarlier(service, filename):
    # Find and delete earlier versions
    response = service.files().list(q="name='" + filename + "'",
                                    spaces='drive', 
                                    fields="files(id, name)").execute()
    
    files = response.get('files', [])
    if len(files) > 0:
        print("Found", len(files), "earlier revisions on Google Drive, deleting them")
        for f in files:
                service.files().delete(fileId=f.get('id')).execute()

def _uploadFile(service, filename):
    # Upload file
    file_metadata = {'name': filename, 'mimeType': 'application/vnd.google-apps.spreadsheet'}
    media = MediaFileUpload(filename, mimetype='text/csv')
    file = service.files().create(body=file_metadata,
                                        media_body=media,
                                        fields='id').execute()
    fid = file.get('id')
    print('top5 sheet uploaded with File ID: %s' % fid)
    return fid