'''
Фабричный метод (Factory Method)
Фабричный метод — это порождающий паттерн, который определяет интерфейс
для создания объекта, но позволяет подклассам изменять тип создаваемогообъекта.

📌 Простыми словами:
У вас есть общий интерфейс для создания объектов.
Конкретные классы решают, какой объект создавать.
Избавляет клиентский код от привязки к конкретным классам.

📌 Примеры из жизни
Логистика (доставка грузов)
Есть общий интерфейс Transport (грузовик, корабль, самолет).
Подклассы (RoadLogistics, SeaLogistics) решают, какой транспорт создать.
UI-библиотеки (кнопки, поля ввода)
Windows и macOS рендерят кнопки по-разному.
Фабричный метод создает нативные элементы под ОС.
ORM (разные типы БД)
Подключение к PostgreSQL vs SQLite — фабрика выбирает нужный адаптер.

'''


from abc import ABC, abstractmethod

# Абстрактный класс Транспорта
class Transport(ABC):
    @abstractmethod
    def deliver(self) -> str:
        pass

# Конкретные реализации транспорта
class Truck(Transport):
    def deliver(self) -> str:
        return "Доставка грузовиком"

class Ship(Transport):
    def deliver(self) -> str:
        return "Доставка кораблем"

# Абстрактный класс Логистики (с фабричным методом)
class Logistics(ABC):
    @abstractmethod
    def create_transport(self) -> Transport:
        pass

    def plan_delivery(self) -> str:
        transport = self.create_transport()
        return f"Планируем доставку: {transport.deliver()}"

# Конкретные фабрики
class RoadLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Truck()

class SeaLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Ship()

# Использование
road_logistics = RoadLogistics()
print(road_logistics.plan_delivery())  # Планируем доставку: Доставка грузовиком

sea_logistics = SeaLogistics()
print(sea_logistics.plan_delivery())  # Планируем доставку: Доставка кораблем

