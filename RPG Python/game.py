import messages
from enemies import *
import os
from random import choice


class Game:
    def __init__(self, player):
        self.player = player
        self.running = False
        self.initialize_enemies()

    def start(self):
        self.running = True

    def initialize_enemies(self):
        self.enemies = [Goblin('Zort'), Goblin('Fazz'), Wolf('Pierun'), Bandit('Slawek')]

    def update(self):
        os.system('cls')

        total_enemies_before = len(self.enemies)
        self.enemies = [e for e in self.enemies if e.health > 0]
        total_enemies_after = len(self.enemies)
        self.player.enemies_slain += total_enemies_before - total_enemies_after

        if len(self.enemies) == 0:
            print(messages.ALL_ENEMIES_DEAD)
            self.running = False

        if self.player.health <= 0:
            print(messages.YOU_DIED)
            self.running = False

    def perform_next_action(self):
        os.system('cls')

        user_message = f'Your stats:\n\t{self.player}\n\n'
        user_message += 'Remaining enemies:\n'
        user_message += '\n'.join(f'\t{i}. {enemy}' for i, enemy in enumerate(self.enemies, 1))
        user_message += '\n\nSelect your action:\n'
        user_message += f'\t- 1 to {len(self.enemies)} - attack selected enemy\n'
        user_message += f'\t- h - heal yourself and one random enemy (1 HP)\n'
        user_message += f'\t- s - skip (random enemy will attack you anyway!)\n'

        print(user_message)

        possible_inputs = 'sh'

        if len(self.enemies) > 0:
            possible_inputs += ''.join(str(i) for i in range(1, len(self.enemies) + 1))

        selection = input('Selection: ')

        while (selection not in possible_inputs) or len(selection) != 1:
            print(messages.INVALID_VALUE)
            selection = input('Selection: ')

        print()

        if selection == 's':
            enemy = choice(self.enemies)
            print(str.format(messages.ATTACK_INFO, enemy.name, type(enemy).__name__, self.player.name, type(self.player).__name__))
            enemy.perform_attack(self.player)
        elif selection == 'h':
            enemy = choice(self.enemies)
            print(str.format(messages.HEAL_INFO, enemy.name, type(enemy).__name__))
            self.player.update_health(1)
            enemy.update_health(1)
        else:
            i = int(selection) - 1
            enemy = self.enemies[i]
            print(str.format(messages.ATTACK_INFO, self.player.name, type(self.player).__name__, enemy.name, type(enemy).__name__))
            self.player.perform_attack(enemy)

        print()
        input(messages.PRESS_ENTER_TO_CONTINUE)