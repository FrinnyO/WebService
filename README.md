# WebService

### Структура проекта

Проект использует Django в качестве веб-фреймворка. Стили и скрипты подключены с использованием Bootstrap.

### Содержание

На данный момент в проекте реализовано приложение **catalog** внутри которого присутствуют страницы:

1. ***home***
2. ***contacts***
3. ***single_product***
4. ***add_product***
5. ***product_confirm_delete***

А также приложение **blog** внутри которого присутствуют страницы:

1. ***articles_list***
2. ***article_detail***
3. ***article_create***
4. ***article_update***
5. ***article_confirm_delete***

В проекте реализована авторизация и регистрация.

### Подключенные маршруты

1. localhost:8000/catalog/home/
2. localhost:8000/catalog/contacts/
3. localhost:8000/catalog/product/<pk>/
4. localhost:8000/catalog/product/<pk>/update/
5. localhost:8000/catalog/product/<pk>/delete/
6. localhost:8000/catalog/add_product/
7. localhost:8000/blog/articles_list/
8. localhost:8000/blog/article_detail/
9. localhost:8000/blog/article_create/
10. localhost:8000/blog/article_update/
11. localhost:8000/blog/article_confirm_delete/
12. localhost:8000/admin/

### База данных
Проект использует базу данных PostgreSQL. Для создания базы данных и применения миграций используйте следующие команды:
```
python manage.py makemigrations
```
```
python manage.py migrate
```

### Модели
Созданы и зарегистрированы модели ***Category***, ***Product***, ***Contact*** в приложении **catalog**.


Модель ***Product*** связана с моделью ***Category*** через внешний ключ.

Форма для добавления товара находится в файле ***forms.py*** в приложении **catalog**.

Создана и зарегистрирована модель ***Article*** в приложении **blog**.

Созданы фикстуры для заполнения базы данных тестовыми данными. Для добавления данных в базу данных используйте следующую команду:

```
python manage.py add_products
```

```
python manage.py add_articles
```

### Аутентификация

Настроена система регистрации и авторизации. При успешной регистрации отправляется письмо на почту с подтверждением.

Для быстрого создания пользователя-администратора воспользуйтесь командой:

```
python manage.py createadmin
```

### Права доступа

Права доступа настроены таким образом, чтобы только владелец продукта и модератор могли удалять продукт. Редактировать продукт может только владелец

Для быстрого создания группы модераторов воспользуйтесь командой:

```
python manage.py create_moderators_group
```


### Переменные окружения

Для работы с базой данных необходимо создать файл ***.env*** в корневой директории проекта и добавить следующие переменные:

**SECRET_KEY= ключ из settings.py**

**DEBUG= True либо False**

**DATABASE_NAME = Имя данное созданной базе данных**

**DATABASE_USER = Имя пользователя базы данных**

**DATABASE_PASSWORD = Пароль от базы данных**

**DATABASE_HOST = Имя хоста**

**DATABASE_PORT = Номер порта базы данных**

Для работы отправки почты необходимо настроить почтовый сервер со следующими настройками в файле ***.env***

**EMAIL_HOST=**
**EMAIL_USE_TLS=**
**EMAIL_PORT=**
**EMAIL_HOST_USER=**
**EMAIL_HOST_PASSWORD=**

### Структура проекта:

Проект использует виртуальное окружение ***Poetry***. Информация о зависимостях проекта
находится в файле ***pyproject.toml***. 

Для более простой установки зависимостей рекомендуется использовать виртуальное окружение
Poetry. 

Чтобы установить зависимости используйте  следующую команду:

```
poetry install
```