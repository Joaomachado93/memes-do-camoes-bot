"""
Corre este script para fazer login numa conta e guardar a sessao.
Uso: python3 login_account.py <username>
"""

import json
import subprocess
import sys

from instagrapi import Client


def main():
    if len(sys.argv) < 2:
        print("Uso: python3 login_account.py <username>")
        print("Exemplo: python3 login_account.py memesdocamoes2")
        sys.exit(1)

    username = sys.argv[1]
    password = "Alegria123@123"

    # Mapear username para nome do secret
    secret_map = {
        "memesdocamoes_": "IG_MEMESDOCAMOES_SESSION",
        "memesdocamoes2": "IG_MEMESDOCAMOES2_SESSION",
        "memesdocamoes3": "IG_MEMESDOCAMOES3_SESSION",
        "memesdocamoes4": "IG_MEMESDOCAMOES4_SESSION",
        "memesdocamoes5": "IG_MEMESDOCAMOES5_SESSION",
    }

    secret_name = secret_map.get(username)
    if not secret_name:
        print(f"Username '{username}' nao reconhecido!")
        sys.exit(1)

    print(f"[{username}] A fazer login...")
    print("Se o Instagram pedir um codigo, vai ao teu email e insere-o aqui.")

    cl = Client()
    cl.login(username, password)

    settings = cl.get_settings()
    session_json = json.dumps(settings)
    print(f"[{username}] Login OK!")

    print(f"[{username}] A guardar sessao no GitHub Secret '{secret_name}'...")
    result = subprocess.run(
        ["gh", "secret", "set", secret_name, "--body", session_json],
        capture_output=True,
        text=True,
    )
    if result.returncode == 0:
        print(f"[{username}] Sessao guardada com sucesso!")
    else:
        print(f"[{username}] Erro: {result.stderr}")


if __name__ == "__main__":
    main()
