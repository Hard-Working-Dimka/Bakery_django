# BakeryDjango

**BakeryDjango** — это веб-приложение на основе Django, предназначенное для управления заказами пекарни.

## Особенности

- **Управление заказами**: создание, редактирование информации о тортах.
- **Управление тортами**: создание/сортировка по параметрам.
- **Управление модификациями**: создание/редактирование/сортировка.
- **Управление ссылками**: создание сокращенных ссылок/подсчет количества переходов по коротким ссылкам с помощью сервиса по сокращению ссылок API социальной сети "ВКонтакте".

## Требования

- Python 3.7+
- Django 5.1+
- Установленные зависимости из `requirements.txt`

## Установка

1. Клонируйте репозиторий:

```bash
git clone https://github.com/Hard-Working-Dimka/Bakery_django
cd Bakery_django
```

2. Создайте виртуальное окружение:

```bash
python3 -m venv venv
source venv/bin/activate  # Для Windows: venv\Scripts\activate
```

3. Установите зависимости:

```
pip install -r requirements.txt
```

4. Создайте файл для переменных окружения в корне проекта `.env`. Переменные окружения:

```
SECRET_KEY = REPLACE_ME
VK_ACCESS_TOKEN= REPLACE_ME
```
Персональный ключ API для VK_ACCESS_TOKEN можно получить на сайте [ВКонтакте](https://vk.com/) на странице [разработчиков ВКонтакте](https://vk.com/dev).
Сервисный токен приложения выглядит так:
```
82a02da882a02da882a02da8a981b7f3cc882a082a02da8e4af9c41e8551329276dde72.
```
5. Примените миграции базы данных:

```
cd bakery
python manage.py migrate
```

6. Создайте суперпользователя для доступа к административной панели:

```
python manage.py createsuperuser
```

7. Запустите сервер разработки:

```
python manage.py runserver
```

## Структура проекта:

* `bakery/bakery/` — основной модуль проекта.
* `bakery/api/` — модуль, содержащий реализацию API.
* `bakery/cakes/` — модуль, отвечающий за админ-панель, также определения моделей, сокращение ссылок и подсчет количества переходов по ним.

## API

### Customusers

- `GET /api/customusers/,`: Получить список всех пользователей.
- `POST /api/customusers/`: Создать нового пользователя.
- `GET /api/customusers/{id}/`: Получить данные пользователя по ID.
- `PATCH /api/customusers/{id}/`: Обновить данные пользователя.
- `DELETE /api/customusers/{id}/`: Удалить пользователя.

### Cakes

- `GET /api/cakes/`: Получить список всех тортов с их модификациями.
- `POST /api/cakes/`: Создать новый торт.
- `GET /api/cakes/{id}/`: Получить информацию о торте по ID.
- `PATCH /api/cakes/{id}/`: Обновить данные торта.
- `DELETE /api/cakes/{id}/`: Удалить торт.
- `POST /shorten/`: Создание короткой ссылки. Принимает long_url в теле запроса.
- `GET /s/{short_url}/`: Перенаправление на оригинальный URL по короткой ссылке.

### Orders

- `GET /api/orders/`: Получить список всех заказов.
- `POST /api/orders/`: Добавить новый заказ.
- `GET /api/orders/{id}/`: Получить информацию о заказе по ID.
- `PATCH /api/orders/{id}/`: Обновить данные заказа.
- `DELETE /api/orders/{id}/`: Удалить заказ.

## Модели

### custom-user

Расширенная версия `AbstractUser` с дополнительными полями:

- **Поля**: `telegram_id `, `telegram_name `.

---

### Cake

Представляет торт.

- **Поля**: `name `, `description `,  `ingredients `, `price`, `photo`.

---

### Modifications

Представляет общую модификацию, которая привязана к торту.

- **Связь по внешнему ключу с:** `cake` из модели `Cake`.
- **Поля**: `modification `, `necessary `.

---

### VariablesOfModification

Представляет вариации определенной модификации.

- **Связь по внешнему ключу с:** `modification` из модели `Modifications`.
- **Поля**: `tier `, `price `.

---

### Order

Представляет заказ.

- **Связь по внешнему ключу с:** `customer` из модели `CustomUser`, `cake` из модели `Cake`.
- **Поля**: `address `, `status `, `delivery `, `phone_number `, `created `, `comment `, `total_price `,
  `variables_of_modifications`.

---
### ShortenedURL

Модель для хранения информации о сокращенных ссылках.

- **Поля**: `long_url`, `short_url`, `click_count`, `created_at`.
- **Методы**: `save()`, `get_vk_short_url(long_url)`, `__str__()`.

## Админ-панель

Панель администратора доступна по адресу /admin/ для управления всеми моделями.
