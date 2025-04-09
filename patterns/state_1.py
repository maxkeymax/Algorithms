from abc import ABC, abstractmethod

# Абстрактное состояние
class State(ABC):
    @abstractmethod
    def publish(self, document):
        pass

    @abstractmethod
    def render(self):
        pass

# Конкретные состояния
class Draft(State):
    def publish(self, document):
        print("Перевод документа на модерацию")
        document.set_state(Moderation())

    def render(self):
        print("Показываем черновик (редактируемый)")

class Moderation(State):
    def publish(self, document):
        print("Одобряем и публикуем документ")
        document.set_state(Published())

    def render(self):
        print("Показываем документ в режиме предпросмотра")

class Published(State):
    def publish(self, document):
        print("Документ уже опубликован")

    def render(self):
        print("Показываем финальную версию документа")

# Контекст (Документ)
class Document:
    def __init__(self):
        self._state = Draft()  # Начальное состояние

    def set_state(self, state: State):
        self._state = state

    def publish(self):
        self._state.publish(self)

    def render(self):
        self._state.render()

# Использование
doc = Document()
doc.render()  # Показываем черновик (редактируемый)
doc.publish() # Перевод документа на модерацию
doc.render()  # Показываем документ в режиме предпросмотра
doc.publish() # Одобряем и публикуем документ
doc.render()  # Показываем финальную версию документа
doc.publish() # Документ уже опубликован