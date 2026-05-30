#!/bin/bash

echo "Починаємо розгортання інфраструктури..."

# Зупиняємо старі контейнери
docker-compose down

echo "Збірка та запуск контейнерів..."
docker-compose up -d --build

echo "Усі сервіси запущені!"
echo "-------------------------------------------------"
echo "pgAdmin доступний за адресою: http://localhost:5050"
echo "   Логін: admin@admin.com"
echo "   Пароль: root"
echo "-------------------------------------------------"
echo "Перегляд логів додатку в реальному часі (Ctrl+C для виходу):"

docker-compose logs -f app