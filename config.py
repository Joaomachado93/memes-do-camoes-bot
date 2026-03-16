import os

# Ordem de prioridade das contas (1a = maior prioridade)
ACCOUNTS = [
    {
        "name": "memesdocamoes_",
        "username": os.environ.get("IG_MEMESDOCAMOES_USER", "memesdocamoes_"),
        "password": os.environ.get("IG_MEMESDOCAMOES_PASS", ""),
    },
    {
        "name": "memesdocamoes2",
        "username": os.environ.get("IG_MEMESDOCAMOES2_USER", "memesdocamoes2"),
        "password": os.environ.get("IG_MEMESDOCAMOES2_PASS", ""),
    },
    {
        "name": "memesdocamoes3",
        "username": os.environ.get("IG_MEMESDOCAMOES3_USER", "memesdocamoes3"),
        "password": os.environ.get("IG_MEMESDOCAMOES3_PASS", ""),
    },
    {
        "name": "memesdocamoes4",
        "username": os.environ.get("IG_MEMESDOCAMOES4_USER", "memesdocamoes4"),
        "password": os.environ.get("IG_MEMESDOCAMOES4_PASS", ""),
    },
    {
        "name": "memesdocamoes5",
        "username": os.environ.get("IG_MEMESDOCAMOES5_USER", "memesdocamoes5"),
        "password": os.environ.get("IG_MEMESDOCAMOES5_PASS", ""),
    },
]

# Google Drive folder ID (pasta unica com todos os videos + watermark.png)
DRIVE_FOLDER_ID = os.environ.get("DRIVE_FOLDER_ID", "")

# Extensoes de video aceites
VIDEO_EXTENSIONS = (".mp4", ".mov", ".avi", ".mkv")
