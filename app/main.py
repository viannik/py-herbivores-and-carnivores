from dataclasses import dataclass


@dataclass
class Animal():
    name: str
    health: int = 100
    hidden: bool = False

    alive = []
    def __post_init__(self):
        Animal.alive.append(self)

    def __repr__(self):
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden

class Carnivore(Animal):
    def bite(self, herbivore: Herbivore):
        if not herbivore.hidden and isinstance(herbivore, Herbivore):
            herbivore.health -= 50
            if herbivore.health <= 0:
                Animal.alive.remove(herbivore)
