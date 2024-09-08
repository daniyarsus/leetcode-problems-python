from dataclasses import dataclass


@dataclass(frozen=True)
class Hero:
    name: str
    health: int

    def kick(self) -> str:
        return f"Player {self.name} with {self.health} health kicked!"


hero = Hero("daniyarsus", 18)
print(hero.kick())
