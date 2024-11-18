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

# Запуск сервера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]