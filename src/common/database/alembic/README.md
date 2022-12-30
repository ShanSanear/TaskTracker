Generic single-database configuration.

# How to update database

Run docker container with database:
```
docker compose up db
```

In different terminal, run:
```powershell
$ENV:REVISION_MESSAGE="REVISION_MESSAGE"
docker compose up db_create_migration_file
```

To actually migrate, run:
```powershell
docker compose up db_migrate
```