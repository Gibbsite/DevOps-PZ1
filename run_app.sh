#!/bin/bash

IMAGE_NAME="DevOps-1PZ-Base-Level-FastAPI"
CONTAINER_NAME="DevOps-1PZ-Base-Level-FastAPI-Container"
PORT=8000

echo "Починаємо розгортання додатку..."

# Зупинка та видалення старого контейнера, якщо він існує
if [ $(docker ps -a -q -f name=$CONTAINER_NAME) ]; then
    echo "Зупиняємо та видаляємо старий контейнер $CONTAINER_NAME..."
    docker stop $CONTAINER_NAME
    docker rm $CONTAINER_NAME
fi

echo "Збираємо Docker-образ $IMAGE_NAME..."
docker build -t $IMAGE_NAME .

echo "Запускаємо контейнер..."
docker run -d --name $CONTAINER_NAME -p $PORT:$PORT $IMAGE_NAME

echo "Додаток доступний за адресою: http://localhost:$PORT"