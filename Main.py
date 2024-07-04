from gladiator import Gladiator
from arena import Arena
import random

def choose_arena(arenas):
    while True:
        try:
            choice = int(input("Vyberte arénu (zadejte číslo): "))
            if 1 <= choice <= len(arenas):
                return arenas[choice - 1]
            else:
                print("Neplatná volba arény. Zvolte číslo arény.")
        except ValueError:
            print("Neplatná volba. Zadejte číslo arény.")

def choose_gladiator_type():
    types = ["Mnich", "Druid", "Kouzelník", "Lukostřelec", "Šermíř", "Paladin"]
    print("Dostupné typy gladiátorů:")
    for i, gladiator_type in enumerate(types, 1):
        print(f"{i}. {gladiator_type}")
    
    while True:
        try:
            choice = int(input("Vyberte typ gladiátora (zadejte číslo): "))
            if 1 <= choice <= len(types):
                return types[choice - 1]
            else:
                print("Neplatná volba typu. Zvolte číslo typu.")
        except ValueError:
            print("Neplatná volba. Zadejte číslo typu.")

def main():
    arenas = [
        Arena("Bahenní aréna"),
        Arena("Pouštní aréna"),
        Arena("Mlžná aréna"),
        Arena("Horská aréna"),
        Arena("Ledová aréna")
    ]

    print("Vítejte ve hře Gladiátoři!")
    print("Dostupné arény:")
    for idx, arena in enumerate(arenas, 1):
        print(f"{idx}. {arena.name}")
    
    arena = choose_arena(arenas)
    print(f"\nBoj začíná na aréně: {arena}")

    print("\nVytvoření Gladiátora 1")
    name1 = input("Zadejte jméno gladiátora: ")
    type1 = choose_gladiator_type()
    gladiator1 = Gladiator(name1, type1)

    opponent_type = input("Chcete bojovat proti jinému hráči (P) nebo proti počítači (C)? ").lower()
    if opponent_type == 'p':
        print("\nVytvoření Gladiátora 2")
        name2 = input("Zadejte jméno gladiátora 2: ")
        type2 = choose_gladiator_type()
        gladiator2 = Gladiator(name2, type2)
    else:
        gladiator2 = Gladiator("Computer", random.choice(["Mnich", "Druid", "Kouzelník", "Lukostřelec", "Šermíř", "Paladin"]))

    print(f"\n{gladiator1.name} ({gladiator1.type}) bojuje proti {gladiator2.name} ({gladiator2.type})!\n")

    while gladiator1.health > 0 and gladiator2.health > 0:
        # Player 1's turn
        print(f"Na řadě je hráč {gladiator1.name}")
        print(f"{gladiator1.name} má {gladiator1.mana} many.")
        if gladiator1.ability_cooldown == 0:
            print(f"{gladiator1.special_ability[0]} je k dispozici.")
        
        action1 = input("Vyberte akci (útok/schopnost): ").lower()
        while action1 not in ["útok", "schopnost"]:
            print("Neplatná volba akce. Zvolte 'útok' nebo 'schopnost'.")
            action1 = input("Vyberte akci (útok/schopnost): ").lower()

        if action1 == "útok":
            damage = gladiator1.attack()
            gladiator2.take_damage(damage)
            print(f"{gladiator1.name} udeřil {gladiator2.name} a způsobil {damage:.1f} poškození.")
        elif action1 == "schopnost":
            if gladiator1.ability_cooldown == 0 and gladiator1.mana >= 10:
                gladiator1.use_ability(gladiator2)
            else:
                print(f"{gladiator1.special_ability[0]} není k dispozici.")
                continue

        if gladiator2.health <= 0:
            print(f"{gladiator1.name} vyhrál!")
            break

        print(f"{gladiator2.name} má nyní {gladiator2.health:.1f} zdraví.")

        # Player 2's turn
        print(f"Na řadě je {gladiator2.name}")
        if opponent_type == 'p':
            print(f"{gladiator2.name} má {gladiator2.mana} many.")
            if gladiator2.ability_cooldown == 0:
                print(f"{gladiator2.special_ability[0]} je k dispozici.")
            
            action2 = input("Vyberte akci (útok/schopnost): ").lower()
            while action2 not in ["útok", "schopnost"]:
                print("Neplatná volba akce. Zvolte 'útok' nebo 'schopnost'.")
                action2 = input("Vyberte akci (útok/schopnost): ").lower()
        else:
            if gladiator2.ability_cooldown == 0 and gladiator2.mana >= 10:
                action2 = "schopnost"
            else:
                action2 = "útok"

        if action2 == "útok":
            damage = gladiator2.attack()
            gladiator1.take_damage(damage)
            print(f"{gladiator2.name} udeřil {gladiator1.name} a způsobil {damage:.1f} poškození.")
        elif action2 == "schopnost":
            if gladiator2.ability_cooldown == 0 and gladiator2.mana >= 10:
                gladiator2.use_ability(gladiator1)
            else:
                print(f"{gladiator2.special_ability[0]} není k dispozici.")
                continue

        if gladiator1.health <= 0:
            print(f"{gladiator2.name} vyhrál!")
            break

        print(f"{gladiator1.name} má nyní {gladiator1.health:.1f} zdraví.")

        # Apply arena events and display the results only if there is a change
        health_change_1 = arena.apply_random_bonus(gladiator1)
        if health_change_1:
            print(f"{health_change_1} {gladiator1.name} má nyní {gladiator1.health:.1f} zdraví.")
        
        health_change_2 = arena.apply_random_bonus(gladiator2)
        if health_change_2:
            print(f"{health_change_2} {gladiator2.name} má nyní {gladiator2.health:.1f} zdraví.")

        gladiator1.regenerate_mana()
        gladiator2.regenerate_mana()
        gladiator1.decrease_cooldown()
        gladiator2.decrease_cooldown()

if __name__ == "__main__":
    main()
