<div align="center" width="100%">
    <img src="./public/icon.svg" width="128" alt="Uptime Kuma Logo" />
</div>

# Uptime Kuma

Uptime Kuma is an easy-to-use self-hosted monitoring tool.

<a target="_blank" href="https://github.com/louislam/uptime-kuma"><img src="https://img.shields.io/github/stars/louislam/uptime-kuma?style=flat" /></a> <a target="_blank" href="https://hub.docker.com/r/louislam/uptime-kuma"><img src="https://img.shields.io/docker/pulls/louislam/uptime-kuma" /></a> <a target="_blank" href="https://hub.docker.com/r/louislam/uptime-kuma"><img src="https://img.shields.io/docker/v/louislam/uptime-kuma/2?label=docker%20image%20ver." /></a> <a target="_blank" href="https://github.com/louislam/uptime-kuma"><img src="https://img.shields.io/github/last-commit/louislam/uptime-kuma" /></a> <a target="_blank" href="https://opencollective.com/uptime-kuma"><img src="https://opencollective.com/uptime-kuma/total/badge.svg?label=Open%20Collective%20Backers&color=brightgreen" /></a>
[![GitHub Sponsors](https://img.shields.io/github/sponsors/louislam?label=GitHub%20Sponsors)](https://github.com/sponsors/louislam) <a href="https://weblate.kuma.pet/projects/uptime-kuma/uptime-kuma/">
<img src="https://weblate.kuma.pet/widgets/uptime-kuma/-/svg-badge.svg" alt="Translation status" />
</a>

<img src="https://user-images.githubusercontent.com/1336778/212262296-e6205815-ad62-488c-83ec-a5b0d0689f7c.jpg" width="700" alt="Uptime Kuma Dashboard Screenshot" />

## 🥔 Live Demo

Experience Uptime Kuma in action!

**Demo Server (Frankfurt, Germany):** [https://demo.kuma.pet/start-demo](https://demo.kuma.pet/start-demo)

_Note: This is a temporary live demo; all data will be deleted after 10 minutes. Sponsored by [Uptime Kuma Sponsors](https://github.com/louislam/uptime-kuma#%EF%B8%8F-sponsors)._

## ⭐ Features

- **Comprehensive Monitoring**: Support for HTTP(s), TCP, HTTP(s) Keyword, HTTP(s) JSON Query, WebSocket, Ping, DNS Record, Push, Steam Game Server, Docker Containers, gRPC, MongoDB, MySQL, PostgreSQL, Redis, RabbitMQ, MQTT, SNMP, and more.
- **Modern UI/UX**: Fast, reactive, and beautiful dashboard powered by Vue 3 and Bootstrap 5.
- **Extensive Notifications**: Integrate with **95+ notification services**, including Telegram, Discord, Gotify, Slack, Pushover, Email (SMTP), and many others.
- **Fast Intervals**: Monitoring intervals as low as 20 seconds.
- **Global Reach**: [Multi-language support](https://github.com/louislam/uptime-kuma/tree/master/src/lang) with translations for over 70 languages.
- **Status Pages**: Create multiple public status pages and map them to specific domains.
- **Insightful Charts**: Monitor performance with ping charts and response time history.
- **Certificate Monitoring**: Stay informed about SSL/TLS certificate information and expiration.
- **Advanced Security**: Support for 2FA (Two-Factor Authentication).
- **Proxy Support**: Connect through proxies for various monitoring tasks.

## 🔧 Installation

### 🐳 Docker Compose (Recommended)

```bash
mkdir uptime-kuma
cd uptime-kuma
curl -o compose.yaml https://raw.githubusercontent.com/louislam/uptime-kuma/master/compose.yaml
docker compose up -d
```

Uptime Kuma is now accessible at `http://localhost:3001` or `http://<your-ip>:3001`.

> [!WARNING]
> Network File Systems (NFS) are **NOT** supported for data storage. Please use a local directory or volume.

### 🐳 Docker Command

```bash
docker run -d --restart=always -p 3001:3001 -v uptime-kuma:/app/data --name uptime-kuma louislam/uptime-kuma:2
```

To limit exposure to localhost only:

```bash
docker run -d --restart=always -p 127.0.0.1:3001:3001 -v uptime-kuma:/app/data --name uptime-kuma louislam/uptime-kuma:2
```

### 💪 Non-Docker

**Requirements:**

- **Platform**: Major Linux distros (Debian, Ubuntu, Fedora, ArchLinux, etc.), Windows 10+ (x64), Windows Server 2012 R2+ (x64).
- **Node.js**: >= 20.4.0
- **Git**: [Required for cloning]
- **pm2**: Recommended for running in the background.

```bash
# Clone the repository
git clone https://github.com/louislam/uptime-kuma.git
cd uptime-kuma

# Setup the project
npm run setup

# Option 1: Start the server directly
node server/server.js

# Option 2: Run in the background using PM2 (Recommended)
npm install pm2 -g && pm2 install pm2-logrotate
pm2 start server/server.js --name uptime-kuma
```

**Useful PM2 Commands:**

- `pm2 monit`: View console output and performance.
- `pm2 startup && pm2 save`: Set up Uptime Kuma to start on system boot.

### 🛠️ Advanced Installation

For reverse proxy configurations and additional options, please refer to the [Wiki: How to Install](https://github.com/louislam/uptime-kuma/wiki/%F0%9F%94%A7-How-to-Install).

## 🆙 Updating

Stay up-to-date with the latest features and fixes by following the [Update Guide](https://github.com/louislam/uptime-kuma/wiki/%F0%9F%86%99-How-to-Update).

## 🆕 Roadmap

Check out planned features and upcoming milestones: [GitHub Milestones](https://github.com/louislam/uptime-kuma/milestones).

## ❤️ Sponsors

A huge thank you to our sponsors!

<img src="https://uptime.kuma.pet/sponsors?v=6" alt="Uptime Kuma Sponsors" />

## 🖼 Screenshots

| Light Mode                                                                                 | Status Page                                                                                                                                      |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| <img src="https://uptime.kuma.pet/img/light.jpg" width="350" alt="Light Mode Dashboard" /> | <img src="https://user-images.githubusercontent.com/1336778/134628766-a3fe0981-0926-4285-ab46-891a21c3e4cb.png" width="350" alt="Status Page" /> |

| Settings                                                                            | Telegram Notifications                                                                      |
| ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| <img src="https://louislam.net/uptimekuma/2.jpg" width="350" alt="Settings Page" /> | <img src="https://louislam.net/uptimekuma/3.jpg" width="350" alt="Telegram Notification" /> |

## 💡 Motivation

- Created as a self-hosted alternative to tools like "Uptime Robot".
- Built to provide a stable and well-maintained monitoring solution.
- Designed with a focus on a modern, responsive UI.
- Developed to explore the capabilities of Vue 3, Vite, Bootstrap 5, and WebSockets.

If you find Uptime Kuma useful, please consider giving it a ⭐!

## 🗣️ Support & Discussion

For general questions and technical support, please use the following resources:

- **Documentation/Wiki**: [Official Wiki](https://github.com/louislam/uptime-kuma/wiki)
- **GitHub Issues**: [Bug Reports & Feature Requests](https://github.com/louislam/uptime-kuma/issues)
- **Reddit**: [r/UptimeKuma](https://www.reddit.com/r/UptimeKuma/)

_Note: Please avoid sending support requests via email; they will not be answered._

## 🤝 Contributions

### Pull Requests

We welcome pull requests! To keep reviews fast and effective, please make sure you’ve [read our pull request guidelines](https://github.com/louislam/uptime-kuma/blob/master/CONTRIBUTING.md#can-i-create-a-pull-request-for-uptime-kuma).

### Testing

Help us by testing pending pull requests. Learn more on the [Wiki](https://github.com/louislam/uptime-kuma/wiki/Test-Pull-Requests).

### Translations

Want to help translate Uptime Kuma? Visit our [Weblate project](https://weblate.kuma.pet/projects/uptime-kuma/uptime-kuma/).

### Beta Testing

Try out the latest features by testing [Beta Releases](https://github.com/louislam/uptime-kuma/releases).

### Spelling & Grammar

Feel free to correct the grammar in the documentation or code.
My mother language is not English and my grammar is not that great.
