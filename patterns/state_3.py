from fastapi import FastAPI
from abc import ABC, abstractmethod

app = FastAPI()

# Абстрактное состояние заказа
class OrderState(ABC):
    @abstractmethod
    def next(self, order):
        pass

    @abstractmethod
    def status(self) -> str:
        pass

# Конкретные состояния
class NewOrder(OrderState):
    def next(self, order):
        print("Перевод заказа в обработку")
        order.set_state(ProcessingOrder())

    def status(self) -> str:
        return "Новый"

class ProcessingOrder(OrderState):
    def next(self, order):
        print("Заказ отправлен на доставку")
        order.set_state(DeliveredOrder())

    def status(self) -> str:
        return "В обработке"

class DeliveredOrder(OrderState):
    def next(self, order):
        print("Заказ уже доставлен")

    def status(self) -> str:
        return "Доставлен"

# Контекст (Заказ)
class Order:
    def __init__(self):
        self._state = NewOrder()

    def set_state(self, state: OrderState):
        self._state = state

    def next_state(self):
        self._state.next(self)

    def get_status(self) -> str:
        return self._state.status()

# FastAPI роуты
order = Order()  # В реальном приложении храните заказы в БД

@app.post("/order/next")
def move_to_next_state():
    order.next_state()
    return {"status": order.get_status()}

@app.get("/order/status")
def get_order_status():
    return {"status": order.get_status()}