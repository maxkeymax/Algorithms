from abc import ABC, abstractmethod

# Абстрактное состояние плеера
class PlayerState(ABC):
    @abstractmethod
    def play(self, player):
        pass

    @abstractmethod
    def pause(self, player):
        pass

    @abstractmethod
    def stop(self, player):
        pass

# Конкретные состояния
class PlayingState(PlayerState):
    def play(self, player):
        print("Уже воспроизводится")

    def pause(self, player):
        print("Пауза")
        player.set_state(PausedState())

    def stop(self, player):
        print("Остановка")
        player.set_state(StoppedState())

class PausedState(PlayerState):
    def play(self, player):
        print("Продолжаем воспроизведение")
        player.set_state(PlayingState())

    def pause(self, player):
        print("Уже на паузе")

    def stop(self, player):
        print("Остановка")
        player.set_state(StoppedState())

class StoppedState(PlayerState):
    def play(self, player):
        print("Начинаем воспроизведение")
        player.set_state(PlayingState())

    def pause(self, player):
        print("Нельзя поставить на паузу — плеер остановлен")

    def stop(self, player):
        print("Уже остановлен")

# Контекст (Аудиоплеер)
class AudioPlayer:
    def __init__(self):
        self._state = StoppedState()

    def set_state(self, state: PlayerState):
        self._state = state

    def play(self):
        self._state.play(self)

    def pause(self):
        self._state.pause(self)

    def stop(self):
        self._state.stop(self)

# Использование
player = AudioPlayer()
player.play()  # Начинаем воспроизведение
player.pause() # Пауза
player.play()  # Продолжаем воспроизведение
player.stop()  # Остановка
player.pause() # Нельзя поставить на паузу — плеер остановлен