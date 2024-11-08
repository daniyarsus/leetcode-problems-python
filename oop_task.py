class Car:
    def __init__(self, color, size, weight, prize):
        self.color = color
        self.size = size
        self.weight = weight
        self.prize = prize

    def get_color(self):
        return self.color


car = Car("red")
print(car.get_color())


from dataclasses import dataclass


@dataclass(frozen=True)
class CreateCarDTO:
    color: str
    size: int
    weight: int
    prize: int


class CreateCarUseCase:
    def __call__(self, dto: CreateCarDTO) -> None:
        # создаем логику для машины
        ...


car = Car("blue", size=5)