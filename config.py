import os

# Ordem de prioridade das contas (1a = maior prioridade)
ACCOUNTS = [
    {
        "name": "memesdocamoes_",
        "username": "memesdocamoes_",
        "password": os.environ.get("IG_MEMESDOCAMOES_PASS", ""),
        "session": os.environ.get("IG_MEMESDOCAMOES_SESSION", ""),
    },
    {
        "name": "memesdocamoes2",
        "username": "memesdocamoes2",
        "password": os.environ.get("IG_MEMESDOCAMOES2_PASS", ""),
        "session": os.environ.get("IG_MEMESDOCAMOES2_SESSION", ""),
    },
    {
        "name": "memesdocamoes3",
        "username": "memesdocamoes3",
        "password": os.environ.get("IG_MEMESDOCAMOES3_PASS", ""),
        "session": os.environ.get("IG_MEMESDOCAMOES3_SESSION", ""),
    },
    {
        "name": "memesdocamoes4",
        "username": "memesdocamoes4",
        "password": os.environ.get("IG_MEMESDOCAMOES4_PASS", ""),
        "session": os.environ.get("IG_MEMESDOCAMOES4_SESSION", ""),
    },
    {
        "name": "memesdocamoes5",
        "username": "memesdocamoes5",
        "password": os.environ.get("IG_MEMESDOCAMOES5_PASS", ""),
        "session": os.environ.get("IG_MEMESDOCAMOES5_SESSION", ""),
    },
]

# Google Drive folder ID (pasta unica com todos os videos + watermark.png)
DRIVE_FOLDER_ID = os.environ.get("DRIVE_FOLDER_ID", "")

# Extensoes de video aceites
VIDEO_EXTENSIONS = (".mp4", ".mov", ".avi", ".mkv")
