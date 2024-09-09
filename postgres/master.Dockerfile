FROM postgres:16.1

# Копируем наши конфигурационные файлы
COPY ./master/postgresql.conf /etc/postgresql/postgresql.conf
COPY ./master/pg_hba.conf /etc/postgresql/pg_hba.conf

# Устанавливаем правильные разрешения
RUN chown postgres:postgres /etc/postgresql/postgresql.conf /etc/postgresql/pg_hba.conf

# Создаем скрипт инициализации
COPY ./master/init_master.sh /docker-entrypoint-initdb.d/init_master.sh
RUN chmod +x /docker-entrypoint-initdb.d/init_master.sh

# Устанавливаем переменные окружения
ENV POSTGRES_DB=db \
    POSTGRES_USER=user \
    POSTGRES_PASSWORD=password

ENV PGDATA /var/lib/postgresql/data

# Запускаем PostgreSQL с нашей конфигурацией
CMD ["postgres", "-c", "config_file=/etc/postgresql/postgresql.conf"]
