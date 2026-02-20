# Population Service

Population Service - асинхронний парсер даних про населення країн за регіонами.  
Скрипт отримує дані з Wikipedia, зберігає їх у базі даних і дозволяє отримувати статистику за регіонами.

---

## Інсталювання

1. Клонуємо репозиторій:
```bash
git clone https://github.com/HalelaDenys/population_service.git
cd population_service
```
2. Запустить докер та ведіть команди:

```bash
docker-compose up postgres_db -d
docker-compose up get_data
docker-compose up print_data
```