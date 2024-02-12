class Auto:
    """
    Базовый класс для представления автомобилей.
    """

    def __init__(self, make: str, model: str, year: int):
        """
        Конструктор класса Auto.

        :param make: Марка автомобиля.
        :param model: Модель автомобиля.
        :param year: Год выпуска автомобиля.
        """
        self.make = make
        self.model = model
        self.year = year

    def drive(self) -> None:
        """
        Метод для запуска двигателя автомобиля.
        """
        print(f"{self.year} {self.make} {self.model} is driving.")

    def stop(self) -> None:
        """
        Метод для остановки автомобиля.
        """
        print(f"{self.year} {self.make} {self.model} stopped.")

    def repair(self) -> None:
        """
        Метод для проведения ремонта автомобиля.
        """
        print(f"{self.year} {self.make} {self.model} is being repaired.")

    def __str__(self) -> str:
        """
        Магический метод для возврата строкового представления объекта.
        """
        return f"{self.year} {self.make} {self.model}"

    def __repr__(self) -> str:
        """
        Магический метод для возврата строкового представления объекта.
        """
        return f"{self.__class__.__name__}('{self.make}', '{self.model}', {self.year})"


class Truck(Auto):
    """
    Класс для представления грузовых автомобилей.
    """

    def __init__(self, make: str, model: str, year: int, capacity: float):
        """
        Конструктор класса Truck.

        :param make: Марка грузовика.
        :param model: Модель грузовика.
        :param year: Год выпуска грузовика.
        :param capacity: Грузоподъемность грузовика.
        """
        super().__init__(make, model, year)
        self.capacity = capacity

    def load_cargo(self) -> None:
        """
        Метод для загрузки груза в грузовик.
        """
        print(f"{self.year} {self.make} {self.model} is loading cargo.")

    def __str__(self) -> str:
        """
        Перегрузка метода __str__ для класса Truck.
        """
        return f"{super().__str__()} (Truck)"

    def __repr__(self) -> str:
        """
        Перегрузка метода __repr__ для класса Truck.
        """
        return f"{self.__class__.__name__}('{self.make}', '{self.model}', {self.year}, {self.capacity})"

    def tow(self) -> None:
        """
        Метод для буксировки груза грузовиком.
        """
        print(f"{self.year} {self.make} {self.model} is towing.")


class PassengerCar(Auto):
    """
    Класс для представления легковых автомобилей.
    """

    def __init__(self, make: str, model: str, year: int, passengers: int):
        """
        Конструктор класса PassengerCar.

        :param make: Марка легкового автомобиля.
        :param model: Модель легкового автомобиля.
        :param year: Год выпуска легкового автомобиля.
        :param passengers: Количество пассажиров, которое может вместить автомобиль.
        """
        super().__init__(make, model, year)
        self.passengers = passengers

    def carry_passengers(self) -> None:
        """
        Метод для перевозки пассажиров.
        """
        print(f"{self.year} {self.make} {self.model} is carrying {self.passengers} passengers.")

    def __str__(self) -> str:
        """
        Перегрузка метода __str__ для класса PassengerCar.
        """
        return f"{super().__str__()} (Passenger Car)"

    def __repr__(self) -> str:
        """
        Перегрузка метода __repr__ для класса PassengerCar.
        """
        return f"{self.__class__.__name__}('{self.make}', '{self.model}', {self.year}, {self.passengers})"

    def park(self) -> None:
        """
        Метод для парковки автомобиля.
        """
        print(f"{self.year} {self.make} {self.model} is parking.")
