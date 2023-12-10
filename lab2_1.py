from typing import Union

class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        self.init_capacity_volume(capacity_volume)

        if not isinstance(capacity_volume, (int, float)):
            raise TypeError
        if not capacity_volume > 0:
            raise ValueError
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError
        if occupied_volume < 0:
            raise ValueError
        self.occupied_volume = occupied_volume

    def init_capacity_volume(self, capacity_volume: Union[int, float]):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError
        if capacity_volume <= 0:
            raise ValueError
        self.capacity_volume = capacity_volume

if __name__ == "__main__":
    glass_instance = Glass(200, 100)
    print(glass_instance.capacity_volume)
    print(glass_instance.occupied_volume)
