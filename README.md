# Containerized OpenSSL Certbot

*SSL certificates refresher wrapped in Docker.* 

Spawns 3 certificate files (.crt, .pem, .key) in a directory of your choice.

This program spawns self-signed SSL certificates according to your `.env` file and refreshes them.

See [docker-compose.yml](/docker-compose.yml) for more details.

> Note: When using a proxy like Nginx, make sure that the certificates are mounted correctly and are generated before the proxy launches.
> Pulling the image and launching it can take some time. If it doesn’t work the first time, try relaunching the containers with the pre-pulled images.

## Usage

- Clone this repo
- Make `.env` file in this repo from [.env.example](/.env.example), fill the missing fields

### Docker

`docker-compose up` from this repo.

You can use other docker commands, for example passing all the necessary `-e` on `docker run ...`.

The image itself is also available: `docker pull anilev6/certificate_refresher`.

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
