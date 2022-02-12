import messages


def clamp_value(value):
    return value if value > 0 else 1


class Entity:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = clamp_value(health)
        self.attack = clamp_value(attack)
        self.defense = clamp_value(defense)

    def perform_attack(self, other):
        damage_dealt = clamp_value(self.attack - other.defense)
        other.update_health(-damage_dealt)

        if other.health > 0:
            damage_received = clamp_value(other.attack - self.defense)
            self.update_health(-damage_received)

    def update_health(self, value):
        self.health += value
        if self.health <= 0:
            print(str.format(messages.ENTITY_DIED, self.name, type(self).__name__))

    def __str__(self):
        return f'{self.name} ({type(self).__name__}) [HP: {self.health}, ATK: {self.attack}, DEF: {self.defense}]'