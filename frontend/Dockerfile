# Dockerfile
FROM nginx:alpine

# Копіюємо файли у відповідну директорію
COPY templates/index.html /usr/share/nginx/html/index.html
COPY config.json /usr/share/nginx/html/config.json

# Порт, який будемо використовувати
EXPOSE 80
