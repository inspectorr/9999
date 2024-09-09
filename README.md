## 9999
A simple "social network" app for highload tests.

### Development
To run in dev mode using Docker:
```
docker compose up
```

To import people.csv to database:
```
docker compose exec server python -m scripts.import_people
```

### DB replicas
...are included in docker-compose.yml file.

You can customize them in docker-compose.yml file, adding more replicas 
just by adding more services with the same configuration (x-db-replica),
also changing settings.py REPLICA_COUNT value.

The --replicas flag for compose file was not used because due to 
unaviability of using it with easy settings.py routing.

Master promouting is not implemented here.
