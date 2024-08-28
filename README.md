# Containerized OpenSSL Certbot

*SSL certificates refresher wrapped in Docker.*

This program spawns self-signed SSL certificates according to your `.env` file and refreshes them.

## Usage

- Clone this repo
- Make `.env` file in this repo from [.env.example](/.env.example), fill the missing fields

### Docker

`docker-compose up` from this repo.

You can use other docker commands, for example passing all the necessary `-e` on `docker run ...`.

### No Docker, I'm on Linux/Mac

1. Go to [main.py](/main.py) and comment the line below `# Docker container:`
2. `python main.py`

## Telegram

I made this as a fix to Telegram API failing to verify my self-signed SSL certificate:

`SSL error {error:0A000086:SSL routines::certificate verify failed}`

To make Telegram API accept the self-signed certificate, one has to set a webhook with a public key (`.pem` certificate).

```python
cert_file_location = "path/to/selfsigned.pem"
with open(cert_file_location, 'r') as cert_file:
    await bot.setWebhook(url = url, certificate = cert_file)
```

Go to https://api.telegram.org/botYOUR_BOT_TOKEN/getWebhookInfo to check.
