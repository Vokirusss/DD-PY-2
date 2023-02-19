from typing import Union


class Vehicle:
    """
    Базовый класс Автомобиль

    :param color: цвет кузова автомобиля, str
    :param model: название модели автомобиля, str
    :param vehicle_weight: масса без пассажиров и груза в тоннах, int or float
    :param max_speed: максимальная скорость автомобиля в км/ч, int

    :raise: TypeError, если тип входных данных не соответствует предполагаемому типу
    :raise: ValueError, если полученное на вход значение не может соответствовать реальной характеристике

    """
    def __init__(self, model: str, color: str, vehicle_weight: Union[int, float], max_speed: int):
        """ Валидация атрибутов объекта класса Автомобиль """
        if not isinstance(model, str):
            raise TypeError("The model should be a string")
        self._model = model

        if not isinstance(color, str):
            raise TypeError("The color should be a string")
        self._color = color

        if not isinstance(vehicle_weight, tuple([int, float])):
            raise TypeError("The weight should be an int or float")
        if vehicle_weight <= 0:
            raise ValueError("The weight should be positive")
        self._vehicle_weight = vehicle_weight

        if not isinstance(max_speed, int):
            raise TypeError("The max speed should be an int")
        if max_speed <= 0:
            raise ValueError("The max speed should be positive")
        self._max_speed = max_speed

    def __str__(self) -> str:
        return f'This car is a {self._color} {self._model}. Weight: {self._vehicle_weight} tonnes. Max speed: {self._max_speed}.'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}model={self._model!r}, (color={self._color!r}, weight={self._vehicle_weight}, max_speed={self._max_speed})'

    # Защищаем базовые аргументы и даём возможность перезаписи
    # Модель, как в примере с автором книги, менять запрещаем. Остальные менять можно.
    @property
    def model(self) -> str:
        """ Get the model of the vehicle """
        return self._model

    @property
    def color(self) -> str:
        """ Get the color of the vehicle """
        return self._color

    @color.setter
    def color(self, new_color: str) -> None:
        """ Set a new color of the vehicle """
        if not isinstance(new_color, str):
            raise TypeError("The color should be a string")
        self._color = new_color

    @property
    def weight(self) -> int or float:
        """ Get the weight of the vehicle """
        return self._vehicle_weight

    @weight.setter
    def weight(self, new_weight: Union[int, float]) -> None:
        """ Set a new weight of the vehicle """
        if not isinstance(new_weight, tuple([int, float])):
            raise TypeError("The weight should be an int or float")
        if new_weight <= 0:
            raise ValueError("The weight should be positive")
        self._vehicle_weight = new_weight

    @property
    def max_speed(self) -> int:
        """ Get the maximum speed of the vehicle """
        return self._max_speed

    @max_speed.setter
    def max_speed(self, new_max_speed: int) -> None:
        if not isinstance(new_max_speed, int):
            raise TypeError("The max speed should be an int")
        if new_max_speed <= 0:
            raise ValueError("The max speed should be positive")
        self._max_speed = new_max_speed

    def max_kinetic_energy(self) -> float:
        """
        Возвращает кинетическую энергию автомобиля при максимальной скорости в Джоулях.
        Наследуется в неизменном виде дочерними классами.
        """
        return (self._vehicle_weight * (self.max_speed / 3.6) ** 2) / 2

    def fuel_consumption(self) -> float:
        """
        Возвращает расход топлива автомобиля в литрах на 100 км.
        Этот метод может быть переопределен в дочерних классах для расчета расхода топлива
        иным образом.
        """
        return None

    def calculate_payload(self, max_weight: Union[int, float]) -> float:
        """
        Возвращает максимальную загрузку автомобиля в тоннах.
        Максимальная загрузка автомобиля рассчитывается как разница между максимально допустимой массой
        и его собственной массой (без пассажиров и груза).

        :param max_weight: максимально допустимая масса в тоннах, int or float

        """
        # Параметр max_weight указан здесь, а не в __init__, чтобы передавать его только тогда, когда нужно
        # Поскольку pydantic не используется, сделать этот аргумент Optional не можем
        # Выносить в отдельную init-функцию тоже пробовал, но тогда просит передать аргумент при вызове в основном __init__
        if not isinstance(max_weight, tuple([int, float])):
            raise TypeError("The maximal weight should be an int or float")
        if max_weight <= 0:
            raise ValueError("The maximal weight should be positive")
        self.max_weight = max_weight
        return self.max_weight - self._vehicle_weight


class Car(Vehicle):
    """
    Дочерний класс Легковой автомобиль

    :param body_type: тип кузова автомобиля, str

    """
    def __init__(self, model, color, vehicle_weight, max_speed, body_type: str):  # аннотацию типов убрал, чтобы меньше дублировать код
        super().__init__(model, color, vehicle_weight, max_speed)  # вызываем конструктор родительского класса для его расширения
        if not isinstance(body_type, str):
            raise TypeError("The body type should be a string")
        self.body_type = body_type

    def __str__(self) -> str:
        return f'{super().__str__()} Body type: {self.body_type}.'  # наследуем и дополняем __str__

    def __repr__(self) -> str:  # а вот метод __repr__ придется перегружать из-за одной скобки
        return f'{self.__class__.__name__}(model={self._model!r}, color={self._color!r}, weight={self._vehicle_weight}, max_speed={self._max_speed}, body_type={self.body_type!r})'

    def calculate_payload(self, max_weight: Union[int, float]) -> float:
        """ Допустим, для легкового автомобиля грузоподъёмность хотим возвращать не в тоннах,
         а в килограммах """
        super(Car, self).calculate_payload(max_weight)
        return (self.max_weight - self._vehicle_weight) * 1000


class Truck(Vehicle):
    """
    Дочерний класс Грузовой автомобиль

    :param trailer: наличие прицепа (есть или нет), bool

    """
    def __init__(self, color, model, vehicle_weight, max_speed, trailer: bool):
        super().__init__(color, model, vehicle_weight, max_speed)
        if not isinstance(trailer, bool):
            raise TypeError("The trailer availability should be a string")
        self.trailer = trailer

    def __str__(self) -> str:
        return f'{super().__str__()} The ability to attach a trailer: {self.trailer}'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(color={self._color!r}, model={self._model!r}, weight={self._vehicle_weight}, max_speed={self._max_speed}, trailer={self.trailer})'

    def calculate_payload(self, max_weight: Union[int, float]) -> float:
        super(Truck, self).calculate_payload(max_weight)
        return self.max_weight - self._vehicle_weight / 2  # просто для примера


if __name__ == "__main__":
    vehicle_example = Vehicle('Volvo', 'blue', 2, 200)
    print(vehicle_example)

    car_example = Car('Nissan', 'gray', 1.9, 180, 'sedan')
    print(car_example)
    print("Payload:", car_example.calculate_payload(5), "kg")

    truck_example = Truck('Scania', 'orange', 8.19, 163, True)
    print(truck_example)
    print("Max kinetic energy:", truck_example.max_kinetic_energy())  # наследуемый метод
    print("Payload:", truck_example.calculate_payload(15))  # перегружаемый метод
