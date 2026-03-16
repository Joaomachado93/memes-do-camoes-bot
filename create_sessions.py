"""
Corre este script NO TEU COMPUTADOR para gerar sessoes do Instagram.
As sessoes sao guardadas como GitHub Secrets automaticamente.

Uso: python3 create_sessions.py
"""

import json
import subprocess
import sys

from instagrapi import Client

ACCOUNTS = [
    ("memesdocamoes2", "IG_MEMESDOCAMOES2_SESSION"),
    ("memesdocamoes3", "IG_MEMESDOCAMOES3_SESSION"),
    ("memesdocamoes4", "IG_MEMESDOCAMOES4_SESSION"),
    ("memesdocamoes5", "IG_MEMESDOCAMOES5_SESSION"),
    ("memesdocamoes_", "IG_MEMESDOCAMOES_SESSION"),
]

PASSWORD = "Alegria123@123"


def create_session(username, password):
    """Faz login e retorna a sessao como JSON."""
    cl = Client()
    cl.login(username, password)
    settings = cl.get_settings()
    cl.logout()
    return json.dumps(settings)


def save_to_github_secret(secret_name, secret_value):
    """Guarda o valor como GitHub Secret."""
    result = subprocess.run(
        ["gh", "secret", "set", secret_name, "--body", secret_value],
        capture_output=True,
        text=True,
    )
    return result.returncode == 0


def main():
    skip = input("Queres saltar a conta memesdocamoes_? (s/n): ").strip().lower()

    for username, secret_name in ACCOUNTS:
        if skip == "s" and username == "memesdocamoes_":
            print(f"[{username}] A saltar...")
            continue

        print(f"\n[{username}] A fazer login...")

        try:
            session_json = create_session(username, PASSWORD)
            print(f"[{username}] Login OK!")

            print(f"[{username}] A guardar sessao no GitHub Secret '{secret_name}'...")
            if save_to_github_secret(secret_name, session_json):
                print(f"[{username}] Secret guardado!")
            else:
                print(f"[{username}] ERRO ao guardar secret!")

        except Exception as e:
            print(f"[{username}] ERRO: {e}")
            continue

    print("\n=== Sessoes criadas! ===")


if __name__ == "__main__":
    main()
