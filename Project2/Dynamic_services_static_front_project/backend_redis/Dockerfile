# Вибір базового образу
FROM python:3.10-slim

# Встановлення залежностей
RUN apt-get update && apt-get install -y libpq-dev gcc

# Встановлення pip
RUN pip install --upgrade pip

# Створення та налаштування робочого каталогу
WORKDIR /app

# Копіюємо файли проекту в контейнер
COPY . /app/

# Встановлюємо залежності з requirements.txt
RUN pip install -r requirements.txt

# Перевіряємо, що все працює коректно
RUN python manage.py check

# Налаштовуємо порти
EXPOSE 8001

# Запуск сервісу
CMD ["gunicorn", "backend_redis.wsgi:application", "--bind", "0.0.0.0:8001"]
