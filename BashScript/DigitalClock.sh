#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
CYAN='\033[0;36m'

while true
do
    clear
    echo -e "${GREEN}========================="
    echo -e "${CYAN}         Clock"
    echo -e "${RED}        $(date +%T)"
    echo -e "${GREEN}========================="
    sleep 1s
done
