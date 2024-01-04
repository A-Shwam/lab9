# Используйте официальный образ Python с Alpine Linux
FROM python:3.8-alpine

# Установите рабочий каталог в /app
WORKDIR /app

# Добавьте текущий каталог (с вашим Flask приложением) в контейнер в /app
ADD . /app

# Установите зависимости Python
RUN pip install --no-cache-dir flask

# Сделайте порт 5000 доступным для мира вне этого контейнера
EXPOSE 5000

# Запустите приложение, когда контейнер запускается
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
