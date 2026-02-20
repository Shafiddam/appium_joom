# Базовый образ с Python
FROM python:3.11-slim

# Установка Appium (для мобильных тестов)
#RUN npm install -g appium

# Копирование зависимостей Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование кода тестов
COPY . /app
WORKDIR /app

# Запуск тестов
CMD ["pytest", "tests/"]