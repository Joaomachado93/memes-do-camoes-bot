import json

from instagrapi import Client


def publish_reel(username, password, video_path, session_json=None, caption=""):
    """Publica um Reel no Instagram.
    Se session_json for fornecido, usa a sessao guardada.
    Caso contrario, faz login com username/password."""

    cl = Client()

    if session_json:
        settings = json.loads(session_json)
        cl.set_settings(settings)
        cl.login(username, password)
    else:
        cl.login(username, password)

    media = cl.clip_upload(video_path, caption=caption)

    return media.pk
