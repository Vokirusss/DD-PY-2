import doctest


class Vehicle(object):
    """
    Создание и подготовка к работе объекта Транспортное средство.

    :param color: цвет транспортного средства, string
    :param doors: количество дверей, integer
    :param vtype: тип транспортного средства, string
    :raise: TypeError, если тип входных данных не соответствует предполагаемому типу
    :raise: ValueError, если полученное на вход значение не может соответствовать реальной характеристике

    """
    def __init__(self, color: str, doors: int, vtype: str):
        """Валидация атрибутов объекта Транспортное средство"""
        if not isinstance(color, str):
            raise TypeError("Укажите корректное название цвета текстом.")
        self.color = color
        if not isinstance(doors, int):
            raise TypeError("Значение количества дверей должно быть целочисленным.")
        if doors < 0:
            raise ValueError("Значение количества дверей должно быть больше нуля.")
        self.doors = doors
        if not isinstance(vtype, str):
            raise TypeError("Укажите название вида транспортного средства словами")
        self.vtype = vtype

    def drive(self):
        """Drive the vehicle"""
        return "I'm driving a %a %s!" % (self.color, self.vtype)  # магическая команда %

    def brake(self):
        """Stop the vehicle"""
        return "%s braking" % self.vtype


class User(object):
    """
    Создание и подготовка к работе объекта Пользователь.

    :param username: имя пользователя, str
    :param age: возраст, int
    :param country: страна пользователя, str

    """
    def __init__(self, username: str, age: int, country: str):
        """Валидация атрибутов объекта Транспортное средство"""
        if not isinstance(username, str):
            raise TypeError("Имя пользователя должно содержать только буквы!")
        if len(username) < 2:
            raise ValueError("Имя пользователя должно состоять не менее, чем из двух букв.")
        self.username = username

        if not isinstance(age, int):
            raise TypeError("Укажите возраст пользователя в целочисленном формате.")
        if age <= 0:
            raise ValueError("Возраст пользователя не может быть менее года.")
        if age > 100:
            raise ValueError("Вы уверены, что люди столько живут?")
        self.age = age

        if not isinstance(country, str):
            raise TypeError("Укажите корректное название страны в формате string.")
        self.country = country

    def create_account(self) -> dict:
        """Создание аккунта пользователя"""
        pass

    def account_info(self) -> str:
        return "The user is %a, %a y.o., from %a" % (self.username, self.age, self.country)

    def delete_account(self):
        """Удаление существующего аккаунта"""
        pass


class Weapon:
    """
    Создание и подготовка к работе объекта Оружие

    :param weapon_type: вид оружия, str
    :param damage: урон от одного удара/выстрела, int
    :param clip_capacity: вместительность магазина, int
    :param firing_rate: скорострельность (количество выстрелов в минуту), float

    """
    def __init__(self, weapon_type: str, damage: int, clip_capacity: int, firing_rate: float):
        """Валидация атрибутов объекта Оружие"""
        if not isinstance(weapon_type, str):
            raise TypeError
        self.weapon_type = weapon_type

        if not isinstance(damage, int):
            raise TypeError
        if damage < 0:
            raise ValueError
        self.damage = damage

        if not isinstance(clip_capacity, int):
            raise TypeError
        if clip_capacity <= 0:
            raise ValueError
        self.clip_capacity = clip_capacity
        # Can I check all the values in one line through "or"? (DRY)

        if not isinstance(firing_rate, float):
            raise TypeError
        if firing_rate < 0:
            raise ValueError
        self.firing_rate = firing_rate

    def get_weapon(self) -> str:
        """Присвоение единицы оружия персонажу"""
        return "You've got a %a with damage %s" % (self.weapon_type, self.clip_capacity)

    def weapon_info(self):
        """Вывод карточки с характеристиками оружия"""
        pass

    def shot_count(self, shots: int) -> (str, int):
        """
        Подсчет количества оставшихся в магазине патронов
        Метод вычисляет количество патронов, оставшихся в обойме после совершения заданного количества выстрелов.

        :param shots: количество совершенных выстрелов, int
        :return: фраза 'Осталось патронов до перезарядки' и результат вычисления

        Пример:
        >>> weapon1.shot_count(2)
        Осталось патронов до перезарядки: 4

        """
        cur_num_of_bullets = self.clip_capacity  # текущее количество патронов (по умолчанию полная обойма)
        if shots > cur_num_of_bullets:
            raise ValueError("Потребуется перезарядка")
        cur_num_of_bullets -= shots
        print("Осталось патронов до перезарядки:", cur_num_of_bullets)


if __name__ == "__main__":
    # Инициализируем по одному экземпляру каждого класса
    car = Vehicle("blue", 5, "car")
    print(car.drive())

    user1 = User("Steve", 19, "USA")
    print(user1.account_info())

    weapon1 = Weapon("pistol", 5, 6, 3.2)
    print(weapon1.get_weapon())
    weapon1.shot_count(2)  # метод с расчетом для теста

    doctest.testmod()  # не выдает ошибок
