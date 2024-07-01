# gladiator.py
import random

class Gladiator:
    def __init__(self, name, weapon, armor):
        self.name = name
        self.health = 100
        self.strength = 20
        self.weapon = self.validate_weapon(weapon)
        self.armor = self.validate_armor(armor)

    def equip_weapon(self):
        if self.weapon == "meč":
            self.strength += 10
        elif self.weapon == "sekera":
            self.strength += 15
        elif self.weapon == "kopí":
            self.strength += 5

    def equip_armor(self):
        if self.armor == "lehká":
            self.health += 10
        elif self.armor == "střední":
            self.health += 20
        elif self.armor == "těžká":
            self.health += 30

    def attack(self):
        damage = random.randint(1, self.strength)
        if random.random() < 0.1:
            damage *= 2
            print(f"Kritický zásah! {self.name} způsobil dvojnásobné poškození.")
        return damage

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0

    def validate_weapon(self, weapon_choice):
        valid_weapons = ["meč", "sekera", "kopí"]
        while weapon_choice.lower() not in valid_weapons:
            print("Neplatná volba zbraně. Zvolte 'meč', 'sekeru' nebo 'kopí'.")
            weapon_choice = input(f"Vyberte zbraň pro {self.name} (meč/sekera/kopí): ")
        return weapon_choice.lower()

    def validate_armor(self, armor_choice):
        valid_armors = ["lehká", "střední", "těžká"]
        while armor_choice.lower() not in valid_armors:
            print("Neplatná volba brnění. Zvolte 'lehká', 'střední' nebo 'těžká'.")
            armor_choice = input(f"Vyberte brnění pro {self.name} (lehká/střední/těžká): ")
        return armor_choice.lower()
    