# Memes do Camoes Bot

Bot que publica automaticamente Reels no Instagram a partir de videos no Google Drive, com watermark.

## Contas (por ordem de prioridade)
1. memesdocamoes_
2. memesdocamoes2
3. memesdocamoes3
4. memesdocamoes4
5. memesdocamoes5

## Horarios de publicacao
- 08:00
- 12:00
- 18:00
- 21:00

## Estrutura do Google Drive

```
📁 Instagram/
  🖼️ watermark.png        <- watermark (centrado em baixo)
  📁 memesdocamoes_/
    🎬 video1.mp4
  📁 memesdocamoes2/
    🎬 video1.mp4
  📁 memesdocamoes3/
    🎬 video1.mp4
  📁 memesdocamoes4/
    🎬 video1.mp4
  📁 memesdocamoes5/
    🎬 video1.mp4
```

## Configuracao

### 1. Google Drive
- Criar uma Service Account no Google Cloud Console
- Partilhar a pasta "Instagram" com o email da Service Account
- Exportar o JSON da Service Account

### 2. Instagram
- Cada conta deve ser Business/Creator
- Cada conta ligada a uma Pagina do Facebook
- App registada no Meta Developer Portal com Instagram Graph API
- Gerar tokens de acesso de longa duracao para cada conta

### 3. GitHub Secrets
| Secret | Descricao |
|--------|-----------|
| `GOOGLE_SERVICE_ACCOUNT_JSON` | JSON da Service Account |
| `DRIVE_FOLDER_ID` | ID da pasta raiz "Instagram" no Drive |
| `IG_MEMESDOCAMOES_TOKEN` | Token da conta memesdocamoes_ |
| `IG_MEMESDOCAMOES_ID` | User ID da conta memesdocamoes_ |
| `IG_MEMESDOCAMOES2_TOKEN` | Token da conta memesdocamoes2 |
| `IG_MEMESDOCAMOES2_ID` | User ID da conta memesdocamoes2 |
| `IG_MEMESDOCAMOES3_TOKEN` | Token da conta memesdocamoes3 |
| `IG_MEMESDOCAMOES3_ID` | User ID da conta memesdocamoes3 |
| `IG_MEMESDOCAMOES4_TOKEN` | Token da conta memesdocamoes4 |
| `IG_MEMESDOCAMOES4_ID` | User ID da conta memesdocamoes4 |
| `IG_MEMESDOCAMOES5_TOKEN` | Token da conta memesdocamoes5 |
| `IG_MEMESDOCAMOES5_ID` | User ID da conta memesdocamoes5 |
