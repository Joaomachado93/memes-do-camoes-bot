from instagrapi import Client


def publish_reel(username, password, video_path, caption=""):
    """Publica um Reel no Instagram usando username e password.
    Retorna o media ID se sucesso."""

    cl = Client()
    cl.login(username, password)

    media = cl.clip_upload(video_path, caption=caption)

    cl.logout()

    return media.pk
