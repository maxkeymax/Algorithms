'''
Singleton — это порождающий паттерн, который гарантирует, что у класса
есть только один экземпляр, и предоставляет глобальную точку доступак нему.
Где используется?
Подключения к БД (чтобы не создавать новые соединения на каждый запрос).
Кэши (Redis, Memcached).
Логгеры (один логгер на весь сервис).
Конфигурации приложения (глобальные настройки).

'''

class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


# Проверка
a = Singleton()
b = Singleton()
print(a is b)  # True (это один и тот же объект)
