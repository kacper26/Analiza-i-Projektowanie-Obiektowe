from base_entity import Entity


class Goblin(Entity):
    def __init__(self, name, health=3, attack=2, defense=1):
        super().__init__(name, health, attack, defense)


class Wolf(Entity):
    def __init__(self, name, health=4, attack=3, defense=1):
        super().__init__(name, health, attack, defense)


class Bandit(Entity):
    def __init__(self, name, health=5, attack=2, defense=2):
        super().__init__(name, health, attack, defense)