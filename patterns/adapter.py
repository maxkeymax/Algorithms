'''
Адаптер — это структурный паттерн, который позволяет объектам с несовместимыми
интерфейсами работать вместе.
📌 Простыми словами:
Это как переходник между розетками (USB-C ↔ USB-A).
Адаптер "оборачивает" один интерфейс и делает его совместимым с другим.

'''


from fastapi import FastAPI

app = FastAPI()

# Старая версия API (v1)
class OldExternalAPI:
    def fetch_old_data(self) -> str:
        return "data_from_old_api"

# Новая версия API (v2)
class NewExternalAPI:
    def get_data(self) -> dict:
        return {"data": "data_from_new_api"}

# Адаптер для новой версии API → старый интерфейс
class NewApiAdapter:
    def __init__(self, new_api: NewExternalAPI):
        self.new_api = new_api

    def fetch_old_data(self) -> str:
        new_data = self.new_api.get_data()
        return new_data["data"]

# Роут FastAPI
@app.get("/data")
def get_data(use_new_api: bool = False):
    if use_new_api:
        api = NewApiAdapter(NewExternalAPI())
    else:
        api = OldExternalAPI()
    return {"result": api.fetch_old_data()}