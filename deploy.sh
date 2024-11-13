#!/bin/bash
# Перезапускаємо Docker контейнери за допомогою Docker Compose

cd project1

# Оновлюємо контейнери, зупиняємо старі та запускаємо нові
docker-compose down
docker-compose up -d --build