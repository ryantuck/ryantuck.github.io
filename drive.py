import os
import json
from pathlib import Path

from googleapiclient.discovery import build
from google.oauth2 import service_account


def service():
    """
    Return base service object.
    """
    creds = service_account.Credentials.from_service_account_info(
        info=json.loads(os.environ['GOOGLE_SERVICE_ACCOUNT_JSON']),
    )
    return build('drive', 'v3', credentials=creds)


def ls(q=None):
    """
    List files.
    """
    # TODO support paginatikon
    page_token = None
    svc = service()
    files = []
    while True:
        result = svc.files().list(q=q, pageToken=page_token).execute()
        files += result['files']
        page_token = result.get('nextPageToken')
        if not page_token:
            return files


def folders():
    """
    """
    return ls(q="mimeType = 'application/vnd.google-apps.folder'")


def files(folder_id):
    """
    List files in given folder.
    """
    return ls(q=f"'{folder_id}' in parents")


def get(file_id):
    """
    Get contents of file.
    """
    svc = service()
    return svc.files().get_media(fileId=file_id).execute()



def download_file(file_id, file_name, target_dir, decode=False, binary=True):
    file_contents = get(file_id)
    if decode: # needed for csv files etc
        file_contents = file_contents.decode()
    target_path = Path(target_dir) / Path(file_name)
    print(f'Downloading: {str(target_path)}')
    write_options = 'w'
    if binary: # needed for image files (as opposed to csv)
        write_options = 'wb'
    with open(target_path, write_options) as f:
        f.write(file_contents)

def download_all():
    """
    """
    pngs = [x for x in ls() if x['mimeType'] == 'image/png']
    for png in pngs:

        download_file(
            file_id=png['id'],
            file_name=png['name'].lower().replace(' - ', ' ').replace(' ','-'),
            target_dir='books/candide'
        )
        

if __name__ == '__main__':
    download_all()