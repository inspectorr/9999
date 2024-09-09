#!/bin/bash
set -e

# Копируем конфигурационные файлы в PGDATA
cp /etc/postgresql/postgresql.conf $PGDATA/postgresql.conf
cp /etc/postgresql/pg_hba.conf $PGDATA/pg_hba.conf

# Устанавливаем правильные разрешения
chown postgres:postgres $PGDATA/postgresql.conf $PGDATA/pg_hba.conf
chmod 600 $PGDATA/postgresql.conf $PGDATA/pg_hba.conf

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER replicator WITH REPLICATION PASSWORD 'replicator_password';
    ALTER USER replicator WITH PASSWORD 'replicator_password';
EOSQL

echo "Content of pg_hba.conf:"
cat $PGDATA/pg_hba.conf

echo "Reloading PostgreSQL configuration"
pg_ctl reload

echo "Waiting for configuration to reload..."
sleep 5

echo "PostgreSQL configuration after reload:"
psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c "SHOW hba_file;"
psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c "SELECT * FROM pg_hba_file_rules;"