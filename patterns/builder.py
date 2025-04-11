class Pizza:
    def __init__(self):
        self.size = None
        self.cheese = False
        self.pepperoni = False
        self.mushrooms = False

    def __str__(self):
        return (f"Пицца: размер={self.size}, сыр={self.cheese}, "
                f"пепперони={self.pepperoni}, грибы={self.mushrooms}")

# Строитель для Pizza
class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_size(self, size):
        self.pizza.size = size
        return self  # Возвращаем self для чейнинга

    def add_cheese(self):
        self.pizza.cheese = True
        return self

    def add_pepperoni(self):
        self.pizza.pepperoni = True
        return self

    def add_mushrooms(self):
        self.pizza.mushrooms = True
        return self

    def build(self):
        return self.pizza

# Использование
builder = PizzaBuilder()
pizza = (builder
         .set_size("L")
         .add_cheese()
         .add_pepperoni()
         .build())

print(pizza)  # Пицца: размер=L, сыр=True, пепперони=True, грибы=False