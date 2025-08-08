import random

class Pokemon:
    """Basic Pokemon class"""

    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def lose_hp(self, damage):
        """Reduce HP after damage"""
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def alive(self):
        """Check if Pokemon is alive"""
        return self.hp > 0


def show_health(player, enemy, turn):
    """Display health of both"""
    print(f"\n--- Turn {turn} ---")
    print(f"Your {player.name}: {player.hp} HP")
    print(f"Enemy {enemy.name}: {enemy.hp} HP")


def player_turn(player, enemy):
    """Player's moves, pausing after each"""
    while player.alive():
        print(f"\n{player.name}'s turn!")
        print("1. Attack")
        print("2. Heal")
        move = input("Pick 1 or 2: ")

        if move == "1":
            damage = player.attack + random.randint(0, 10)
            enemy.lose_hp(damage)
            print(f"{player.name} hits for {damage} damage!")

            if not enemy.alive():
                print(f"{enemy.name} is knocked out!")

        elif move == "2":
            heal = 20
            player.hp += heal
            print(f"{player.name} heals {heal} HP!")

        yield


def enemy_turn(player, enemy):
    """Enemy's moves, simple AI"""
    while enemy.alive():
        print(f"\n{enemy.name}'s turn!")

        if enemy.hp < 30:
            heal = 15
            enemy.hp += heal
            print(f"{enemy.name} heals {heal} HP!")
        else:
            damage = enemy.attack + random.randint(0, 10)
            player.lose_hp(damage)
            print(f"{enemy.name} hits for {damage} damage!")

            if not player.alive():
                print(f"{player.name} is knocked out!")

        yield


def game():
    """Run the battle"""
    print("Pokemon Battle with Coroutines!")
    print("See how they take turns!\n")

    # Characters
    pikachu = Pokemon("Pikachu", 100, 20)
    charmander = Pokemon("Charmander", 90, 25)

    print(f"Battle starts: {pikachu.name} vs {charmander.name}!")

    # Turns
    player_moves = player_turn(pikachu, charmander)
    enemy_moves = enemy_turn(pikachu, charmander)

    turn_count = 0

    while pikachu.alive() and charmander.alive():
        turn_count += 1
        show_health(pikachu, charmander, turn_count)

        # Player
        next(player_moves)
        if not charmander.alive():
            break

        input("Press Enter for enemy turn...")

        # Enemy
        next(enemy_moves)
        if not pikachu.alive():
            break

        input("Press Enter for next turn...")

    print("\n" + "=" * 25)
    if pikachu.alive():
        print("YOU WIN!")
    else:
        print("YOU LOSE!")
    print("=" * 25)


if __name__ == "__main__":
    game()
