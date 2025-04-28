# 📄 Spear Phishing Exercise – Lab Environment Setup

This project sets up a controlled environment to simulate a spear phishing attack for cybersecurity training. It uses Docker to run the necessary services inside the SEED Ubuntu VM.

---

#  Quick Start

```bash
# Open your SEED VM
cd ~/spear-phishing-exercise

# Make sure start.sh is executable
chmod +x start.sh

# Launch the environment
./start.sh
```
- Access Mailpit inbox: http://localhost:8025

- Access phishing site (after SET clone): http://localhost:8080
---

# Prerequisites
Before starting, make sure your SEED VM has the following installed:

- ✅ Docker

- ✅ Docker Compose

- ✅ Git

- ✅ A browser installed (Chromium or Firefox)

If Docker or Git are missing, install them with:
```bash
sudo apt update
sudo apt install docker.io docker-compose git -y
```
Start Docker service (if not running);
```bash
sudo systemctl start docker
sudo systemctl enable docker

```
---
# 🛠️ Environment Overview
The lab consists of two Docker containers:

| Container|  Purpose  |
|:-----||------:|
| spearphish  | Runs Social Engineering Toolkit (SET) + Apache server |
| mailpit  |  mailpit	Provides a fake SMTP server + web inbox  |

All services run locally and offline for maximum safety.
---
# How to Set Up the Environment
1. Open your SEED VM
2. Clone this repository
3. Open a terminal and navigate to the project directory
  `cd ../spear-phishing-exercise`
4. Make `start.sh` executable if not already:
   `chmod +x start.sh`
5. Start the environment
   `./start.sh`
This will:
- Build the `spearphish` container
- Pull the `mailpit `container
- Launch both containers on a Docker network
---
# 🌐 Accessing Services
- Mailpit Web Inbox (for phishing emails):
http://localhost:8025

- Phishing Website (hosted by SET after cloning a page):
http://localhost:8080

