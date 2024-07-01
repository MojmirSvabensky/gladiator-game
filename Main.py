import random
from gladiator import Gladiator
from Arena import Arena

def main():
    print("Vítejte ve hře Gladiátoři!")
    print("Dostupné arény:")
    print("1. Lesní aréna")
    print("2. Pouštní aréna")
    print("3. Mlžná aréna")

    arena_choice = int(input("Vyberte arénu (zadejte číslo): "))
    if arena_choice == 1:
        arena = Arena("Lesní aréna")
    elif arena_choice == 2:
        arena = Arena("Pouštní aréna")
    elif arena_choice == 3:
        arena = Arena("Mlžná aréna")
    else:
        print("Neplatná volba arény.")
        return

    print(f"\nBoj začíná na aréně: {arena}\n")

    gladiator1 = create_gladiator(1)
    gladiator2 = create_gladiator(2)

    print(f"\n{gladiator1.name} bojuje proti {gladiator2.name}!\n")

    while gladiator1.is_alive() and gladiator2.is_alive():
        bonus_damage_g1 = arena.apply_random_bonus(gladiator1)
        bonus_damage_g2 = arena.apply_random_bonus(gladiator2)

        if not gladiator2.is_alive():
            break

        attack(gladiator1, gladiator2)
        print(f"\n{gladiator1.name} udeřil {gladiator2.name} a způsobil {gladiator1.last_damage} poškození.")
        print(f"{gladiator2.name} má nyní {gladiator2.health} zdraví.")

        if bonus_damage_g1 is not None and bonus_damage_g1 > 0:
            gladiator1.take_damage(bonus_damage_g1)
            print(f"{arena}: Gladiátor {gladiator1.name} utrpěl dodatečné poškození od arény!")
            print(f"{gladiator1.name} má nyní {gladiator1.health} zdraví.")

        if not gladiator2.is_alive():
            break

        attack(gladiator2, gladiator1)
        print(f"\n{gladiator2.name} udeřil {gladiator1.name} a způsobil {gladiator2.last_damage} poškození.")
        print(f"{gladiator1.name} má nyní {gladiator1.health} zdraví.")

        if bonus_damage_g2 is not None and bonus_damage_g2 > 0:
            gladiator2.take_damage(bonus_damage_g2)
            print(f"{arena}: Gladiátor {gladiator2.name} utrpěl dodatečné poškození od arény!")
            print(f"{gladiator2.name} má nyní {gladiator2.health} zdraví.")

    if gladiator1.is_alive():
        print(f"\n{gladiator2.name} je mrtvý! {gladiator1.name} vyhrál!\n")
    else:
        print(f"\n{gladiator1.name} je mrtvý! {gladiator2.name} vyhrál!\n")

def create_gladiator(number):
    name = input(f"Vytvoření Gladiátora {number}\nZadejte jméno gladiátora: ")

    weapon = None
    while weapon not in ["meč", "sekera", "kopí"]:
        weapon = input(f"Vyberte zbraň pro {name} (meč/sekera/kopí): ").lower()
        if weapon not in ["meč", "sekera", "kopí"]:
            print("Neplatná volba zbraně. Zvolte 'meč', 'sekeru' nebo 'kopí'.")

    armor = None
    while armor not in ["lehká", "střední", "těžká"]:
        armor = input(f"Vyberte brnění pro {name} (lehká/střední/těžká): ").lower()
        if armor not in ["lehká", "střední", "těžká"]:
            print("Neplatná volba brnění. Zvolte 'lehká', 'střední' nebo 'těžká'.")

    return Gladiator(name, weapon, armor)

def attack(attacker, defender):
    damage = attacker.attack()
    defender.take_damage(damage)
    attacker.last_damage = damage

if __name__ == "__main__":
    main()
