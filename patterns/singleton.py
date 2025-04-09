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