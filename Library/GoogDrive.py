import os.path
from googleapiclient.discovery import build, MediaFileUpload
from Library.GoogAuth import _authentication


def UploadToGDrive(filename):
    """Upload the top 5 cast members into a Google Spreadsheet
    """
    service = build('drive', 'v3', credentials=_authentication())

    # Find and delete earlier versions
    response = service.files().list(q="name='" + filename + "'",
                                    spaces='drive', 
                                    fields="files(id, name)").execute()
    
    files = response.get('files', [])
    if len(files) > 0:
        print("Found", len(files), "earlier revisions on Google Drive, deleting them")
        for f in files:
                service.files().delete(fileId=f.get('id')).execute()



    # Upload file
    file_metadata = {'name': filename}
    media = MediaFileUpload(filename, mimetype='text/csv')
    file = service.files().create(body=file_metadata,
                                        media_body=media,
                                        fields='id').execute()
    print('top5.csv uploaded with File ID: %s' % file.get('id'))