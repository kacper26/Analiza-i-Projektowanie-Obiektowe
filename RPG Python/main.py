from player import Player
from game import Game
import messages


def main():
    player = Player('Kacper', 10, 3, 2)

    game = Game(player)
    game.start()

    while game.running:
        game.perform_next_action()
        game.update()

    print(str.format(messages.FINAL_STATS, player.enemies_slain, player.health))

    if player.health > 0:
        print(f'\n\t{messages.VICTORY}\n')


if __name__ == '__main__':
    main()