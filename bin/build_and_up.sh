#!/usr/bin/bash

red='\u001b[31m'
green='\e[92m'
yellow='\u001b[33m'
reset="\\033[0m \n"

printf "${yellow}Gerando file Requirements...${reset}"
poetry export --with dev --format=requirements.txt --output=requirements.txt

printf "${yellow}Create required network...${reset}"
docker network create manager || true

printf "${yellow}Subindo infraestrutura via docker-compose...${reset}"
if ! docker-compose up -d --force-recreate --build --remove-orphans -V; then
    printf "${red}ERROR: Ocorreu um erro ao subir o projeto${reset}"
    exit 1
fi
printf "${green}Build sucessfuly${reset}"