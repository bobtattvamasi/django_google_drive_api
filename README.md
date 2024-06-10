# Тестовое задание: Создание файла в Google Drive

## Описание

Данный проект представляет собой реализацию API-метода для создания файла в Google Drive.

## Перед установкой

Предварительно нужно создать Гугл аккаунт пустой и авторизовать приложение, чтобы получить токены  
Создание пустого Google аккаунта:

1. Перейдите на страницу создания аккаунта Google: https://support.google.com/mail/answer/56256?hl=en  
<details> 
<summary>2. Перейдите на страницу Google Cloud Platform Console: https://console.cloud.google.com/ </summary> 
2.1 Войдите в свой пустой Google аккаунт.   

2.2. Выберите проект или создайте новый.

2.3. В меню слева выберите "APIs & Services".  

2.4. Нажмите кнопку "Enable APIs and Services".

2.5. Введите в поле поиска "Google Drive API".

2.6. Выберите "Google Drive API" из списка.

2.7. Нажмите кнопку "Enable".

2.8. В меню слева выберите "Credentials".

2.9. Нажмите кнопку "Create Credentials".

2.10. Выберите "OAuth client ID".

2.11. Выберите "Web application" как тип приложения.

2.12. Введите название приложения.

2.13. (Опционально) Добавьте URL-адреса, на которые будет перенаправляться пользователь после авторизации.

2.14. Нажмите кнопку "Create".

</details>

## Инсталяция  

Убедитесь, что на вашем компьютере установлены:  
Python 3.11 
pip  
Docker  
Git  
PostgreSQL  
Создайте папку для проекта и клонируйте репозиторий.
Примените миграции Django: ./manage.py migrate  
Создайте суперпользователя Django: ./manage.py createsuperuser  
Запустите сервер Django: ./manage.py runserver  
Запустите брокер сообщений celery: celery -A nova_test_project worker -l info  

API-метод будет доступен по адресу: http://localhost:8000/google_drive/create/  

## Функциональность

* API-метод доступен по POST-запросу.
* Параметры запроса:
    * `data`: Текстовое содержимое файла
    * `name`: Название файла
    * `username`: Имя пользователя
* Сохраняет информацию о созданных файлах в базе данных PostgreSQL.
* Использует Celery для асинхронной обработки задач создания файлов. 
* То ли еще будет...

## Технологии

* Python 3.11
* Django 3.2
* Celery 5.4
* Redis 5.0
* Docker
* GitLab CI/CD
* PostgreSQL 10

## Запуск

1. Клонируйте репозиторий.
2. Создайте файл `.env` и добавьте туда необходимые секретные ключи (токены доступа Google Drive, JWT-секрет).
3. Запустите Docker Compose: `docker-compose up -d`
4. Создайте пользователя в Django admin.
5. Получите JWT-токен для пользователя.
6. Отправьте POST-запрос на API-метод, используя JWT-токен и параметры `data`, `name` и `user_id`.

## Тестирование

1. Запустите тесты Django: `./manage.py test`

## Пример POST-запросов на сервер:  

curl -X POST https://d87c-2405-4802-7196-8930-31b7-99c8-4492-7219.ngrok-free.app/google_drive/create-file/ -H "Content-Type: application/json" -d '{"username": "bob", "name": "file.txt", "data": "This is the content of my file."}'

## Лицензия

MIT
