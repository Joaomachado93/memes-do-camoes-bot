import json
import os
import tempfile

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload

from config import DRIVE_FOLDER_ID, VIDEO_EXTENSIONS, STATE_FILE_NAME


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


def get_next_video(service, folder_id):
    """Retorna o primeiro video disponivel na pasta (por nome)."""
    videos = get_all_videos(service, folder_id)
    return videos[0] if videos else None


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


# --- State management (guardar rotacao no Drive) ---

def _find_state_file(service, folder_id):
    """Encontra o ficheiro state.json no Drive."""
    query = (
        f"'{folder_id}' in parents "
        f"and name = '{STATE_FILE_NAME}' "
        f"and trashed = false"
    )
    results = service.files().list(q=query, fields="files(id)").execute()
    files = results.get("files", [])
    return files[0]["id"] if files else None


def load_state(service, folder_id):
    """Carrega o estado (indice da proxima conta na rotacao)."""
    file_id = _find_state_file(service, folder_id)
    if not file_id:
        return {"next_account_index": 0}

    path = download_file(service, file_id, STATE_FILE_NAME)
    with open(path, "r") as f:
        return json.load(f)


def save_state(service, folder_id, state):
    """Guarda o estado no Drive (cria ou atualiza state.json)."""
    tmp_dir = tempfile.mkdtemp()
    state_path = os.path.join(tmp_dir, STATE_FILE_NAME)

    with open(state_path, "w") as f:
        json.dump(state, f)

    media = MediaFileUpload(state_path, mimetype="application/json")

    file_id = _find_state_file(service, folder_id)
    if file_id:
        service.files().update(fileId=file_id, media_body=media).execute()
    else:
        file_metadata = {
            "name": STATE_FILE_NAME,
            "parents": [folder_id],
        }
        service.files().create(body=file_metadata, media_body=media).execute()
