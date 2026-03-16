import json
import os
import tempfile

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

from config import DRIVE_FOLDER_ID, VIDEO_EXTENSIONS


def get_drive_service():
    """Autentica e retorna o servico do Google Drive."""
    creds_json = os.environ.get("GOOGLE_SERVICE_ACCOUNT_JSON", "")
    creds_info = json.loads(creds_json)
    creds = service_account.Credentials.from_service_account_info(
        creds_info, scopes=["https://www.googleapis.com/auth/drive"]
    )
    return build("drive", "v3", credentials=creds)


def get_all_videos(service, folder_id):
    """Retorna todos os videos na pasta, ordenados por nome."""
    query = (
        f"'{folder_id}' in parents "
        f"and trashed = false "
        f"and mimeType contains 'video/'"
    )
    results = (
        service.files()
        .list(q=query, fields="files(id, name, mimeType)", orderBy="name")
        .execute()
    )
    files = results.get("files", [])

    return [
        f for f in files
        if any(f["name"].lower().endswith(ext) for ext in VIDEO_EXTENSIONS)
    ]


def download_file(service, file_id, file_name):
    """Faz download de um ficheiro do Drive para um ficheiro temporario."""
    request = service.files().get_media(fileId=file_id)
    tmp_dir = tempfile.mkdtemp()
    file_path = os.path.join(tmp_dir, file_name)

    with open(file_path, "wb") as f:
        downloader = MediaIoBaseDownload(f, request)
        done = False
        while not done:
            _, done = downloader.next_chunk()

    return file_path


def delete_file(service, file_id):
    """Apaga um ficheiro do Google Drive."""
    service.files().delete(fileId=file_id).execute()


def download_watermark(service, folder_id):
    """Faz download do watermark.png da pasta."""
    query = (
        f"'{folder_id}' in parents "
        f"and name = 'watermark.png' "
        f"and trashed = false"
    )
    results = service.files().list(q=query, fields="files(id, name)").execute()
    files = results.get("files", [])

    if not files:
        return None

    return download_file(service, files[0]["id"], "watermark.png")
