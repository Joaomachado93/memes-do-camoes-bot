"""
Script de teste: publica apenas na conta memesdocamoes2.
"""

from config import ACCOUNTS, DRIVE_FOLDER_ID
from drive_utils import (
    delete_file,
    download_file,
    download_watermark,
    get_all_videos,
    get_drive_service,
)
from instagram import publish_reel
from watermark import apply_watermark


def main():
    print("=== TESTE - Memes do Camoes Bot ===")

    service = get_drive_service()

    # Buscar videos
    videos = get_all_videos(service, DRIVE_FOLDER_ID)
    if not videos:
        print("Sem videos na pasta. A sair.")
        return

    print(f"{len(videos)} video(s) encontrado(s)")

    # Buscar watermark
    watermark_path = download_watermark(service, DRIVE_FOLDER_ID)
    if not watermark_path:
        print("ERRO: watermark.png nao encontrado!")
        return

    # Usar apenas memesdocamoes2 (indice 1)
    account = ACCOUNTS[1]
    video_file = videos[0]
    name = account["name"]

    print(f"\n[{name}] Video: {video_file['name']}")

    try:
        video_path = download_file(service, video_file["id"], video_file["name"])
        print(f"[{name}] Video descarregado")

        video_with_wm = apply_watermark(video_path, watermark_path)
        print(f"[{name}] Watermark aplicado")

        media_id = publish_reel(account["username"], account["password"], video_with_wm)
        print(f"[{name}] Reel publicado! Media ID: {media_id}")

        delete_file(service, video_file["id"])
        print(f"[{name}] Video apagado do Drive")

    except Exception as e:
        print(f"[{name}] ERRO: {e}")

    print("\n=== TESTE Concluido ===")


if __name__ == "__main__":
    main()
