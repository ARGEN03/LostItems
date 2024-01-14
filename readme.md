# Документация по проекту "Потерянные вещи" (LostItem)

Проект "Потерянные вещи" разработан как веб-приложение, где находятся данные по потерянным и найденным вещам. 

Более подробную информацию по разработке нашего проекта можете посмотреть ниже:


## 1. Активация виртуального окружения

Виртуальное окружение создается в папке, где будет реализован проект. Далее необходимо набрать команды на терминале для создания и активации:

```
python3 -m venv venv

. venv/bin/activate
```

## 2. Установка расширений

Для установки сразу нескольких расширений создается текстовый файл **requirements.txt** и все их наименования прописываются в данном файле. Далее через терминал производится их установка по команде:

```
pip install -r requirements.txt
```


## 3. Создание базы данных

Для создания необходимо зайти через терминал в PostgreSql и создать базу данных по следующей команде:

```
CREATE DATABASE <Наименование базы данных>
```

(в данном проекте название БД - lostitem)


## 4. Создание самого проекта

На терминале необходимо прописать следующую команду:

```
django-admin startproject config . 
```

После чего в папке будет создан проект **config** со встроенными папками и файлами


## 5. Создания приложений для нашего проекта

Для создания новых приложений необходимо написать на терминале следующую команду:

```
python3 manage.py startapp <Наименование приложения>      или      ./manage.py startapp <Наименование приложения>
```

В нашем проекте созданы следующие приложения:

    1.	account
    2.	category
    3.	comment
    4.  feedback
    5.  historysearch
    6.  post


## 6. Создание файла ***.env***

Файл **.env** является файлом конфигураций, который используется для хранения конфидициальной информации и настроек самого приложения. Это упрощает управление конфигурацией в различных окружениях и обеспечивает безопасность конфиденциальных данных. 

Для соединения с этими данными в проекте используется библиотека python-decouple

```python
from decouple import config
```

где функция **config** используется для извлечений значений переменных с файла **.env**. (пример данного файла можете посмотреть в файле env_example)


## 7. Загрузка приложений и пакетов в файле settings.py

В данном файле необходимо добавить наши приложения и пакеты в **INSTALLED_APPS**:
```python
INSTALLED_APPS = [
    ...
    #libs
    'rest_framework',
    'rest_framework.authtoken',
    'drf_yasg',

    #apps
    'post',
    'account',
    'category',
    'comment',
    'historysearch',
    'feedback',
]
```

## 8. Создание моделей для приложений

Модели приложений определяют, какие данные будут храниться в нашем приложении. Django использует модели для создания схемы базы данных. Когда вы определяете модель, Django может автоматически создать соответствующую таблицу в базе данных с полями, соответствующими полям модели.

Структура написания кода следующее:

```python
from django.db import models

class NameOfModel(models.Model):
    field1 = models.<Тип данных поля>
    field2 = models.<Тип данных поля>
    ...
```

## 9. Миграции

Миграции используются для обновления схемы базы данных при изменении моделей. После внесения данных в модели в терминале необходимо будет прописать следующие команды для осуществления миграций:

```
python manage.py makemigrations
python manage.py migrate
```

## 10. Создание админа (superuser)

Для создания админа необходимо написать в терминале следующую команду:

```
./manage.py createsuperuser
```

В нашем проекте для создания суперюзера прописываются следующие пункты:
- Email: <наименование электронной почты>
- Username: <имя пользователя>
- Phone number: <номер телефона>
- Password: <пароль>
- Password (again): <подтверждение пороля>


## 11. Запуск сервера разработки Django

В терминале прописываем следующую команду:

```
python3 manage.py runserver
```


# Функционал проекта

Здесь более подробное описание функционала нашего проекта.
***

- ### Account (Пользователь)

***Create***

Для регистрации (создания) пользователя вводятся следующие данные:
- Имя пользователя (username)
- E-Mail
- Номер телефона
- Telegram
- WhatsApp
- Пароль
- Подтверждение пароля

Данная процедура выполняется по 'POST' запросу

***Read***

По 'GET' запросу через http://localhost:8000/account/ можно вывести список  зарегистрированных пользователей

***Update***

По 'PATCH' запросу через http://localhost:8000/account/user_detail/<int:user_id>/ можно будет обновлять данные по id. В случае успешного изменения выводится сообщение: ***'Account is updated'***

***Delete***

По 'DELETE' запросу через http://localhost:8000/account/user_detail/<int:user_id>/ можно будет обновлять данные по id. В случае успешного изменения выводится сообщение: ***'Account is deleted'***

** Также здесь производится авторизация и выход пользователя с программы

***
- ### Category (Категория)

Здесь также выполняется ***CRUD*** функционал. 
- создание новой категории ('POST') - http://localhost:8000/category/
- вывод категории по id ('GET') - http://localhost:8000/category/{id}/
- вывод всех категорий ('GET') - http://localhost:8000/category/
- обновление категории по id ('PUT' AND 'PATCH') - http://localhost:8000/category/{id}/
- удаление категории по id ('DELETE') - http://localhost:8000/category/{id}/

***
- ### Post (посты)

Здесь происходит реализация постов по 2 категориям: FOUND (Найден) и LOST (Потерян).

Также для создания поста ('Create') вводятся следующие данные:
- наименование поста
- описание поста
- категория (выбор по приложению Category)
- изображение
- владелец поста (один из авторизованных пользователей)

 #### Отзывы / комментарии
В данном приложении также может другой пользователь оставить комментарий по определенному посту  по запросу 'POST': http://localhost:8000/post/{id}/comment/

#### Рекомендации

В рекомендациях выводятся посты, которые были загружены ранее и в течении определенного времени не нашли своих владельцев. Вывод будет происходит черз 'GET' запрос: http://localhost:8000/post/posts_after_expiry/

***
- ### Comment (комментарий)

Здесь также производится весь CRUD функционал. 

#### Likes

Авторизованный пользователь может поставить Like на определенный комментарий. 'POST' запрос: http://localhost:8000/comment/{id}/like/

***

- ### HistorySearch (история поиска)

Сам поиск постов происходит через 'GET' запрос по ключевому значению *query* авторизованным пользователем (http://localhost:8000/post/?search={вводимый_запрос}). После сохранения данных можно будет посмотреть по 'GET' запросу и по ссылке: http://localhost:8000/history/search-history/

***

- ### Feedback

Здесь также выполняется весь CRUD функционал.

***
***

## Permission (ограничения) 

Permission относится к механизму контроля доступа, то есть определяет право доступа пользователя к выполнению определенных действий в системе. Данные файлы именуются permission.py и находятся в самих приложениях.

***
## SWAGGER

Swagger является набором инструментов для разработки, проектирования и документирования веб-сервисов. Для добавления его к нашему проекту необходимо воспользоваться пакетом ***drf-yasg***. Необходимо его установить по следующей команде:

```
pip install drf-yasg
```
Далее в проекте в файле settings.py, где находится INSTALLED_APPS необходимо его добавить:

```python
...
'drf_yasg',
...
```
Далее в файле проекта urls.py необходимо прописать следующий код:

```python
...
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="LostItem",
        default_version='v1',
        description="lostitem",
        terms_of_service="https://localhost:8000/swagger/",
        contact=openapi.Contact(email="alina@gmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    ...
    path('swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
```
Далее запускаем сервер и браузере открываем через ссылку: http://localhost:8000/swagger/. После откроется страница со всем нашим функционалом.

***

## Функционал Celery

Celery, в силу своей ассинхноронности, в нашем проекте выполняет функцию поддтерждения email почти, а так же к нему подключена функция отправки письма на почту владельца поста, если ему оставили комментарий.

Для того чтобы celery начал свою работу необходимо скачать брокер, в данном случае мы будем использвать rabbitmq:

```
sudo apt-get update

sudo apt-get install rabbitmq-server

sudo service rabbitmq-server start
```

Так же нужно установить пакеты в виртуальном окружении

```
pip install -r requirements.txt
```

Далее нужно запустить сам celery в отдельном терминале командой:

```
celery -A config worker -l info
```
***в этой команде "config" можно заменить на название репозитория вашего проекта если вы хотите запустить celery в своем проекте***
***а нужно заменить "config" во всех полях в файле celery.py если вы хотите запустить celery в вашем проекте***
