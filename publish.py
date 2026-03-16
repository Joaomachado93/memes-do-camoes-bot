"""
Script principal:
- 1 pasta no Drive com todos os videos + watermark.png
- A cada execucao, distribui os videos pelas contas por prioridade:
  - 1 video  -> memesdocamoes_
  - 2 videos -> memesdocamoes_ + memesdocamoes2
  - 3+ videos -> distribui por todas as contas
- Apos publicar, apaga o video do Drive
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
    print("=== Memes do Camoes Bot ===")

    service = get_drive_service()

    # Buscar todos os videos da pasta
    videos = get_all_videos(service, DRIVE_FOLDER_ID)
    if not videos:
        print("Sem videos para publicar. A sair.")
        return

    print(f"{len(videos)} video(s) encontrado(s)")

    # Buscar watermark
    watermark_path = download_watermark(service, DRIVE_FOLDER_ID)
    if not watermark_path:
        print("ERRO: watermark.png nao encontrado na pasta do Drive!")
        return

    # Distribuir videos pelas contas por prioridade
    num_to_publish = min(len(videos), len(ACCOUNTS))

    for i in range(num_to_publish):
        video_file = videos[i]
        account = ACCOUNTS[i]
        name = account["name"]
        username = account["username"]
        password = account["password"]
        session = account["session"]

        if not password:
            print(f"[{name}] Sem password configurada, a saltar...")
            continue

        print(f"\n[{name}] Video: {video_file['name']}")

        try:
            # Download do video
            video_path = download_file(service, video_file["id"], video_file["name"])
            print(f"[{name}] Video descarregado")

            # Aplicar watermark
            video_with_wm = apply_watermark(video_path, watermark_path)
            print(f"[{name}] Watermark aplicado")

            # Publicar Reel (usa sessao se disponivel)
            media_id = publish_reel(
                username, password, video_with_wm,
                session_json=session if session else None,
            )
            print(f"[{name}] Reel publicado! Media ID: {media_id}")

            # Apagar video do Drive
            delete_file(service, video_file["id"])
            print(f"[{name}] Video apagado do Drive")

        except Exception as e:
            print(f"[{name}] ERRO: {e}")
            continue

    print("\n=== Concluido ===")


if __name__ == "__main__":
    main()
