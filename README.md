# Тестовый проект на FastAPI по EnjAlice

Для тестирования необходимо создать новый Навык в Консоли в Яндекс.Диалогах. 

Там в настройках заполняете все данные, в Бекенд пишете IP-адрес вашего сервера.

Сборка проекта происходит при помощи docker.

```
git clone enjalice-fastapi-test
cd ./enjalice-fastapi-test
docker-compose up
```

Для сборки на локальном компьютере можете использовать ngrok.

```
git clone enjalice-fastapi-test
cd ./enjalice-fastapi-test
docker-compose up
```

В отдельной консоли запускаете ngrok:

```
ngrok http 8000
```

Копируете ``https`` адрес, который запустился на ngrok сервере, и вставляете в Настройках Навыка в Backend Webhook URL.