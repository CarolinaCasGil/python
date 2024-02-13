import time
import random
import requests

def get_pokemon_data(url):
    response = requests.get(url)
    return response.json()

def display_pokemon_names(pokemon_list):
    for i, pokemon in enumerate(pokemon_list):
        print(f"{i+1}. {pokemon['name']}")

def select_pokemon():
    while True:
        user_input = input("Select a Pokemon by number (1-3) or type 'quit' to exit: ")
        if user_input.lower() == 'quit':
            return None
        try:
            selected_pokemon_number = int(user_input)
            if 1 <= selected_pokemon_number <= 3:
                return selected_pokemon_number - 1
            else:
                print("Please enter a valid number.")
        except ValueError:
            print("Please enter a valid number.")

def store_selected_pokemon_attacks(selected_pokemon_number, pokemon_list):
    selected_pokemon_url = pokemon_list[selected_pokemon_number]['url']
    selected_pokemon_details = get_pokemon_data(selected_pokemon_url)
    selected_pokemon_attacks = [attack['move']['name'] for attack in selected_pokemon_details['moves'][:4]]
    return selected_pokemon_attacks

def explore_animation():
    print("Exploring...")
    time.sleep(3)
    print("Enemy Pokemon appeared!")

def get_random_pokemon(max_pokemon_number):
    pokemon_number = random.randint(1, max_pokemon_number)
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_number}"
    pokemon_data = get_pokemon_data(pokemon_url)
    pokemon_name = pokemon_data['name']
    pokemon_attacks = [attack['move']['name'] for attack in pokemon_data['moves'][:4]]
    return pokemon_name, pokemon_attacks

def battle(selected_pokemon_attacks, enemy_pokemon_name, enemy_pokemon_attacks):
    # Inicializar la vida de los Pokémon
    selected_pokemon_health = 100
    enemy_pokemon_health = 100

    while True:
        print("\nChoose an attack for your Pokémon:")
        for i, attack in enumerate(selected_pokemon_attacks):
            print(f"{i+1}. {attack}")
        user_input = input("Enter the number of the attack or type 'quit' to run away: ")
        if user_input.lower() == 'quit':
            print("You ran away from the battle.")
            return False
        try:
            selected_attack_number = int(user_input)
            if 1 <= selected_attack_number <= len(selected_pokemon_attacks):
                selected_attack = selected_pokemon_attacks[selected_attack_number-1]
                enemy_attack = random.choice(enemy_pokemon_attacks)
                print(f"\nYour Pokémon used {selected_attack}! Enemy Pokémon used {enemy_attack}!")
                if selected_attack == enemy_attack:
                    print("It's a tie!")
                elif selected_attack == 'rock' and enemy_attack == 'scissors' or \
                     selected_attack == 'paper' and enemy_attack == 'rock' or \
                     selected_attack == 'scissors' and enemy_attack == 'paper':
                    print("You won!")
                    enemy_pokemon_health -= 10
                    if enemy_pokemon_health <= 0:
                        print(f"\nCongratulations! You defeated {enemy_pokemon_name}!")
                        return True
                else:
                    print("You lost!")
                    selected_pokemon_health -= 10
                    if selected_pokemon_health <= 0:
                        print(f"\nOh no! You lost against {enemy_pokemon_name}...")
                        return False
            else:
                print("Please enter a valid number.")
        except ValueError:
            print("Please enter a valid number.")


def main():
    url = "https://pokeapi.co/api/v2/pokemon?limit=3"
    pokemon_data = get_pokemon_data(url)

    while True:
        display_pokemon_names(pokemon_data['results'])
        selected_pokemon_number = select_pokemon()
        if selected_pokemon_number is None:
            break
        selected_pokemon_attacks = store_selected_pokemon_attacks(selected_pokemon_number, pokemon_data['results'])
        
        print(f"You selected {pokemon_data['results'][selected_pokemon_number]['name']} with attacks: {', '.join(selected_pokemon_attacks)}")
        
        explore_animation()

        enemy_pokemon_name, enemy_pokemon_attacks = get_random_pokemon(100)

        if battle(selected_pokemon_attacks, enemy_pokemon_name, enemy_pokemon_attacks):
            print(f"\nCongratulations! You defeated {enemy_pokemon_name}!")
        else:
            print(f"\nOh no! You lost against {enemy_pokemon_name}...")

if __name__ == "__main__":
    main()