from abc import ABC, abstractmethod

# Абстрактный интерфейс для подключения к БД
class DatabaseConnection(ABC):
    @abstractmethod
    def connect(self) -> str:
        pass

# Конкретные подключения
class PostgreSQLConnection(DatabaseConnection):
    def connect(self) -> str:
        return "Подключение к PostgreSQL"

class SQLiteConnection(DatabaseConnection):
    def connect(self) -> str:
        return "Подключение к SQLite"

# Фабрика БД
class DatabaseFactory(ABC):
    @abstractmethod
    def create_connection(self) -> DatabaseConnection:
        pass

# Конкретные фабрики
class PostgreSQLFactory(DatabaseFactory):
    def create_connection(self) -> DatabaseConnection:
        return PostgreSQLConnection()

class SQLiteFactory(DatabaseFactory):
    def create_connection(self) -> DatabaseConnection:
        return SQLiteConnection()

# Клиентский код
def client_code(factory: DatabaseFactory) -> None:
    connection = factory.create_connection()
    print(connection.connect())

# Использование
postgres_factory = PostgreSQLFactory()
client_code(postgres_factory)  # Подключение к PostgreSQL

sqlite_factory = SQLiteFactory()
client_code(sqlite_factory)  # Подключение к SQLite