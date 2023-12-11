import doctest
from typing import Union, List


class PhysicalObject:
    """
    Class representing a physical object.

    Attributes:
        name (str): The name of the object.
        weight (float): The weight of the object.
        material (str): The material of the object.

    Methods:
        move(destination: str) -> None:
            Move the object to a specified destination.
        interact() -> None:
            Simulate interaction with the object.
    """

    def __init__(self, name: str, weight: float, material: str):
        self.name = name
        self.weight = weight
        self.material = material

    def move(self, destination: str) -> None:
        """
        Move the physical object to a specified destination.

        :param destination: The destination to which the object is being moved.

        Examples:
        >>> obj = PhysicalObject("Table", 50.0, "wood")
        >>> obj.move("Living Room")
        The wood Table is being moved to Living Room.
        """
        print(f"The {self.material} {self.name} is being moved to {destination}.")

    def interact(self) -> None:
        """Simulate interaction with the physical object.

        Examples:
        >>> obj = PhysicalObject("Table", 50.0, "wood")
        >>> obj.interact()
        Someone is interacting with the wood Table.
        """
        print(f"Someone is interacting with the {self.material} {self.name}.")


class LivingBeing:
    """
    Class representing a living being.

    Attributes:
        name (str): The name of the being.
        age (int): The age of the being.
        health (float): The health status of the being.
        occupation (str): The occupation of the being.

    Methods:
        eat(food: str, quantity: Union[int, float]) -> None:
            Simulate eating for the living being.
        sleep(hours: int) -> None:
            Simulate sleeping for the living being.
    """

    def __init__(self, name: str, age: int, health: float, occupation: str):
        self.name = name
        self.age = age
        self.health = health
        self.occupation = occupation

    def eat(self, food: str, quantity: Union[int, float]) -> None:
        """
        Simulate eating for the living being.

        :param food: The type of food being eaten.
        :param quantity: The quantity of food being eaten.

        Examples:
        >>> person = LivingBeing("John Doe", 30, 90.5, "Engineer")
        >>> person.eat("Pizza", 300)
        John Doe is eating 300 grams of Pizza.
        """
        print(f"{self.name} is eating {quantity} grams of {food}.")

    def sleep(self, hours: int) -> None:
        """
        Simulate sleeping for the living being.

        :param hours: The number of hours the being sleeps.

        Examples:
        >>> person = LivingBeing("John Doe", 30, 90.5, "Engineer")
        >>> person.sleep(8)
        John Doe is sleeping for 8 hours.
        """
        print(f"{self.name} is sleeping for {hours} hours.")


class DigitalEntity:
    """
    Class representing a digital entity.

    Attributes:
        name (str): The name of the digital entity.
        creators (List[str]): List of creators of the digital entity.
        version (float): The version of the digital entity.
        programming_language (str): The programming language used for the digital entity.

    Methods:
        update(new_version: float) -> None:
            Update the version of the digital entity.
        interact() -> None:
            Simulate interaction with the digital entity.
    """

    def __init__(self, name: str, creators: List[str], version: float, programming_language: str):
        self.name = name
        self.creators = creators
        self.version = version
        self.programming_language = programming_language

    def update(self, new_version: float) -> None:
        """
        Update the version of the digital entity.

        :param new_version: The new version to update to.

        Examples:
        >>> software = DigitalEntity("AwesomeApp", ["Team A", "Team B"], 2.0, "Python")
        >>> software.update(2.1)
        AwesomeApp is being updated to version 2.1.
        """
        print(f"{self.name} is being updated to version {new_version}.")

    def interact(self) -> None:
        """Simulate interaction with the digital entity.

        Examples:
        >>> software = DigitalEntity("AwesomeApp", ["Team A", "Team B"], 2.0, "Python")
        >>> software.interact()
        Interacting with AwesomeApp software.
        """
        print(f"Interacting with {self.name} software.")


if __name__ == "__main__":
    doctest.testmod()
