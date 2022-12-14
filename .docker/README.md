## MySQL + Adminer

### How to start

- copy and update /.docker/.env.example to .env

```shell
docker-compose up -d
```

- mysql on __localhost:3306__ (or mysql:3306)
- watch adminer on http://localhost:8080

### Stop

```shell
docker-compose down
```

### Check running containers

```shell
docker-compose ps
```

### Get into container (example)

```shell
docker-compose exec mysql bash
```