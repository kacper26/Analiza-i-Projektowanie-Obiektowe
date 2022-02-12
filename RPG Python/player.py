from base_entity import Entity


class Player(Entity):
    def __init__(self, name, health, attack, defense):
        super().__init__(name, health, attack, defense)
        self.enemies_slain = 0