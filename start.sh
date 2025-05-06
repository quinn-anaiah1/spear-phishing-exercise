#!/bin/bash

echo "[*] Building and starting spearphish + mailpit environment ..."
docker-compose up

#wait briefly to ensure Mailpit is up
sleep 6

#run email filler silently
echo "[*] Preloading Mailpit inbox..."
python3 mailpit/cleanup_mailpit.py > /dev/null 2>&1
python3 mailpit/fill_inbox.py > /dev/null 2>&1
