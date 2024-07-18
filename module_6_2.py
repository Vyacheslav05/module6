class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    def __init__(self, owner, _model, _color, _engine_power):
        self.owner: str = owner
        self._model: str = _model
        self._engine_power: int = _engine_power
        self._color: str = _color
        if _color.lower() in Vehicle.__COLOR_VARIANTS:
            self._color = _color.lower()
        else:
            raise ValueError("Invalid color")

    def set_color(self, new_color):
        if new_color.lower() in Vehicle.__COLOR_VARIANTS:
            self._color = new_color.lower()
        else:
            print(f'Нельзя сменить цвет на {new_color}\n')

    def get_model(self):
        return f'Модель {self._model}'

    def get_horsepower(self):
        return f'Мощность двигателя {self._engine_power}'

    def get_color(self):
        return f'Цвет {self._color}'

    def print_info(self):
        print(f'{self.get_model()}\n{self.get_horsepower()}\n{self.get_color()}\nВладелец {self.owner}\n')

class Sedan(Vehicle):
    _PASSENGER_LIMIT = 5

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()

