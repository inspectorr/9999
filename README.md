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

### DB replication
