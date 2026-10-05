FROM python:3.11-slim

# Встановлюємо робочу директорію
WORKDIR /app

# Копіюємо залежності та встановлюємо
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо весь проєкт
COPY . .

# Збираємо статику, виконуємо міграції та завантажуємо фікстури
RUN python manage.py collectstatic --no-input

# Відкриваємо порт
EXPOSE 10000

# Запуск через gunicorn
CMD python manage.py migrate && \
    python manage.py loaddata banks/fixtures/initial_banks.json || true ; \
    gunicorn config.wsgi:application --bind 0.0.0.0:$PORT
