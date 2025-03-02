# BakeryDjango

**BakeryDjango** — это веб-приложение на основе Django, предназначенное для управления заказами пекарни.

## Особенности

- **Управление заказами**: создание, редактирование информации о тортах.
- **Управление тортами**: создание/сортировка по параметрам/
- **Управление модификациями**: создание/редактирование/сортировка

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
python3 -m venv env
source venv/bin/activate  # Для Windows: venv\Scripts\activate
```

Установите зависимости:

```
pip install -r requirements.txt
```

Создайте файл для переменных окружения в корне проекта `.env`. Переменные окружения:

```
SECRET_KEY = 
```

Примените миграции базы данных:

```
python manage.py migrate
```

Создайте суперпользователя для доступа к административной панели:

```
python manage.py createsuperuser
```

Запустите сервер разработки:

```
python manage.py runserver
```

## Структура проекта:

* `bakery/bakery/` — основной модуль проекта.
* `bakery/api/` — модуль, содержащий реализацию API.
* `bakery/cakes/` — модуль, отвечающий админ-панель, также определения моделей.

## API

### Customusers

- `GET /api/customusers/,`: Получить список всех пользователей
- `POST /api/customusers/`: Создать нового пользователя
- `GET /api/customusers/{id}/`: Получить данные пользователя по ID
- `PATCH /api/customusers/{id}/`: Обновить данные пользователя
- `DELETE /api/customusers/{id}/`: Удалить пользователя

### Cakes

- `GET /api/cakes/`: Получить список всех тортов с их модификациями
- `POST /api/cakes/`: Создать новый торт
- `GET /api/cakes/{id}/`: Получить информацию о торте по ID
- `PATCH /api/cakes/{id}/`: Обновить данные торта
- `DELETE /api/cakes/{id}/`: Удалить торт

### Orders

- `GET /api/orders/`: Получить список всех заказов
- `POST /api/orders/`: Добавить новый заказ
- `GET /api/orders/{id}/`: Получить информацию о заказе по ID
- `PATCH /api/orders/{id}/`: Обновить данные заказа
- `DELETE /api/orders/{id}/`: Удалить заказ

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
- **Связь ManyToMAny с:** `variables_of_modifications` из модели `VariablesOfModification`.
- **Поля**: `address `, `status `, `delivery `, `phone_number `, `created `, `comment `, `total_price `.

---
## Админ-панель

Панель администратора доступна по адресу /admin/ для управления всеми моделями