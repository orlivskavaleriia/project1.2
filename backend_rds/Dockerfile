FROM python:3.9

# Встановлення залежностей
WORKDIR /app
COPY requirements.txt .  
RUN pip install --no-cache-dir -r requirements.txt

# Копіювання коду
COPY . .

# Встановлення змінних середовища для Django
ENV DJANGO_SETTINGS_MODULE=backend_rds.settings
ENV DEBUG=False

# Копіюємо wait_for_postgres.py в контейнер
COPY ./backend_rds/wait_for_postgres.py /app/wait_for_postgres.py

# Запуск сервера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]  
