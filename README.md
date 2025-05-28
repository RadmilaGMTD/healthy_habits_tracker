# healthy_habits_tracker
healthy_habits_tracker — приложения для приобретения новых полезных привычек с напоминаниями в Telegram. Мотивацией будет определенное вознаграждение (приятная привычка или любое другое вознаграждение).
## Установка
1. Клонируйте репозиторий:
```
git@github.com:RadmilaGMTD/healthy_habits_tracker.git
```
2. Установите зависимости:
```
poetry install
```
3. Настройте переменные окружения (создайте .env)

## Запуск

Сервер разработки:
```
python manage.py runserver
```
Celery worker:
```
celery -A config worker -l info -P eventlet
```
Celery beat (для напоминаний):
```
celery -A config beat -l info
```
## Эндпоинты

1. Регистрация.(`users/create/`)
2. Авторизация.(`users/token/`)
3. Список привычек текущего пользователя с пагинацией.(`habits/`)
4. Список публичных привычек.(`habits/`)
5. Создание привычки.(`habits/create`)
6. Редактирование привычки.(`habits/update/<int:pk>/`)
7. Удаление привычки.(`habits/delete/<int:pk>/`)
8. Детальный просмотр привычки.(`habits/<int:pk>/`)

## Telegram Интеграция
### Как подключить:
1. Найдите нашего бота: `@habits_my_bot`
2. Отправьте команду `/start`

## Документация
Доступна по адресу: `/swagger/` и `/redoc/`
