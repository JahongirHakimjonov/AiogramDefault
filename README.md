## 1️⃣ **DAO — Data Access Object**

**Что это:** отдельный слой (объект), который отвечает **только за доступ к данным** в базе данных.
DAO изолирует SQL-запросы и работу с БД от остальной логики приложения.

**Зачем нужен:**

* Выполняет CRUD-операции (Create, Read, Update, Delete).
* Отделяет бизнес-логику от кода работы с БД.
* Упрощает тестирование и поддержку.

**Пример (Python + SQLAlchemy):**

```python
class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_by_id(self, user_id: int):
        return self.session.query(User).filter_by(id=user_id).first()

    def create(self, username: str):
        user = User(username=username)
        self.session.add(user)
        self.session.commit()
        return user
```

---

## 2️⃣ **RDB — Relational DataBase**

**Что это:** реляционная база данных, где данные хранятся в **таблицах** и имеют **связи** между собой (one-to-many,
many-to-many и т. д.).

**Особенности:**

* Работает на SQL.
* Структура: таблицы → строки (records) и столбцы (columns).
* Использует ключи (Primary Key, Foreign Key).
* Поддерживает принципы **ACID** (атомарность, согласованность, изолированность, надёжность).

**Примеры:** PostgreSQL, MySQL, SQLite, Oracle.

**Пример таблицы:**

| id | name | email                                       |
|----|------|---------------------------------------------|
| 1  | Али  | [ali@example.com](mailto:ali@example.com)   |
| 2  | Валя | [vali@example.com](mailto:vali@example.com) |

---

## 3️⃣ **DTO — Data Transfer Object**

**Что это:** объект, предназначенный **только для передачи данных** между слоями программы или сервисами (например,
между API и фронтендом).
DTO обычно не содержит бизнес-логики, только поля с данными.

**Зачем нужен:**

* Передавать только нужные поля.
* Форматировать данные под конкретный интерфейс (например, API).
* Избегать лишней информации в ответах.

**Пример (Pydantic):**

```python
from pydantic import BaseModel


class UserDTO(BaseModel):
    id: int
    username: str
    email: str
```

---

💡 **Разница в двух словах:**

| Термин | Что делает                         | Где используется     |
|--------|------------------------------------|----------------------|
| DAO    | Работает с базой данных            | Backend / Data layer |
| RDB    | Хранит данные в виде таблиц        | Database             |
| DTO    | Передаёт данные между компонентами | API / Service layer  |

![banner](https://i.postimg.cc/4yCmHLNd/dao-rdb-dto-architecture.png "banner")
![banner](https://i.postimg.cc/zGpb2Fpt/Chat-GPT-Image-8-2025-16-41-47.png "banner")

