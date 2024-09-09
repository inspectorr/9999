FROM postgres:16.1

# Копируем наши конфигурационные файлы
COPY ./replica/postgresql.conf /etc/postgresql/postgresql.conf
COPY ./replica/pg_hba.conf /etc/postgresql/pg_hba.conf

# Устанавливаем правильные разрешения
RUN chown postgres:postgres /etc/postgresql/postgresql.conf /etc/postgresql/pg_hba.conf

# Создаем скрипт инициализации
COPY ./replica/init_replica.sh /docker-entrypoint-initdb.d/init_replica.sh
RUN chmod +x /docker-entrypoint-initdb.d/init_replica.sh

# Устанавливаем переменные окружения
ENV POSTGRES_DB=db \
    POSTGRES_USER=user \
    POSTGRES_PASSWORD=password

# Запускаем PostgreSQL с нашей конфигурацией
CMD ["postgres", "-c", "config_file=/etc/postgresql/postgresql.conf"]
