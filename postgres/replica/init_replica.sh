#!/bin/bash
set -e

until pg_isready -h db_master -p 5432 -U replicator
do
    echo "Waiting for master to become available..."
    sleep 1s
done

rm -rf $PGDATA/*
pg_basebackup -h db_master -D $PGDATA -U replicator -P -v -R -W

cat >> $PGDATA/postgresql.auto.conf <<EOF
primary_conninfo = 'host=db_master port=5432 user=replicator password=replicator_password application_name=replica1'
EOF

touch $PGDATA/standby.signal

chown -R postgres:postgres $PGDATA
chmod 700 $PGDATA