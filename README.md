population_service/
│
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── .env
│
└── src/
    ├── db.py             # SQLAlchemy engine, Base, сесія
    ├── models.py         # ORM-модель Country
    ├── parser.py         # парсер сторінки
    ├── repository.py     # клас для роботи з ORM
    ├── services.py       # логіка load_data та print_data
    ├── get_data.py       # контейнер get_data
    └── print_data.py     # контейнер print_data