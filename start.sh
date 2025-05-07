#!/bin/bash

echo "[*] Building and starting spearphish + mailpit environment ..."
docker-compose up -d

# Function to check if a service is ready (optional, improved readiness check)
check_service_ready() {
  service_name="$1"
  port="$2"
  timeout=30 # seconds
  start_time=$(date +%s)

  echo "Checking if $service_name is ready on port $port..."
  while true; do
    if nc -z localhost "$port"; then
      echo "$service_name is ready."
      return 0
    fi
    elapsed=$(( $(date +%s) - start_time ))
    if [ "$elapsed" -gt "$timeout" ]; then
      echo "Timeout waiting for $service_name to become ready."
      return 1
    fi
    sleep 1
  done
}

# Wait for mailpit and mailpit2 to be ready.
check_service_ready "mailpit" 1025
check_service_ready "mailpit2" 1125 # Or the port you configured for mailpit2

#wait briefly to ensure Mailpit is up

echo "[*] Copying login html"
docker cp ./phishing_login/fake_login.html spearphish-env:/var/www/html/index.html
docker cp ./phishing_login/thank_you.html spearphish-env:/var/www/html/thank_you.html
docker cp ./phishing_login/app.py spearphish-env:/var/www/html/app.py

#run email filler silently
echo "[*] Preloading Mailpit inbox..."0
python3 mailpit/cleanup_mailpit.py > /dev/null 2>&1
python3 mailpit/fill_inbox.py > /dev/null 2>&1


echo "[*] Starting login site..."
python3 ./phishing_login/app.py
