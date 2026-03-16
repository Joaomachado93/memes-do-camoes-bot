import json

from instagrapi import Client


def publish_reel(username, password, video_path, session_json=None, caption=""):
    """Publica um Reel no Instagram.
    Se session_json for fornecido, reutiliza a sessao sem login novo."""

    cl = Client()

    if session_json:
        settings = json.loads(session_json)
        cl.set_settings(settings)
        # Relogin com sessao existente - reutiliza cookies/tokens
        cl.set_uuids(settings["uuids"])
        try:
            cl.get_timeline_feed()
            print("  Sessao reutilizada com sucesso")
        except Exception:
            print("  Sessao expirada, a fazer login novo...")
            cl.login(username, password)
    else:
        cl.login(username, password)

    media = cl.clip_upload(video_path, caption=caption)

    return media.pk
