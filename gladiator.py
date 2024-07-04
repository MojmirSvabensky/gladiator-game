import random

class Gladiator:
    def __init__(self, name, type):
        self.name = name
        self.health = 100
        self.mana = 50
        self.dexterity = 10
        self.strength = 20
        self.type = type
        self.weapon, self.armor = self.get_equipment()
        self.special_ability = self.get_special_ability()
        self.ability_cooldown = 0
        self.apply_equipment_effects()

    def get_equipment(self):
        equipment = {
            "Mnich": ("Holé ruce", "Lehké brnění"),
            "Druid": ("Magická hůl", "Lehké brnění"),
            "Kouzelník": ("Kouzelná hůl", "Lehké brnění"),
            "Lukostřelec": ("Luk", "Lehké brnění"),
            "Šermíř": ("Meč", "Střední brnění"),
            "Paladin": ("Meč a štít", "Těžké brnění")
        }
        return equipment[self.type]

    def get_special_ability(self):
        abilities = {
            "Mnich": ("Chi výbuch", 3),
            "Druid": ("Přeměna", 3),
            "Kouzelník": ("Elementální bouře", 3),
            "Lukostřelec": ("Smrtící výstřel", 3),
            "Šermíř": ("Rychlý úder", 3),
            "Paladin": ("Božský zásah", 3)
        }
        return abilities[self.type]

    def apply_equipment_effects(self):
        armor_effects = {
            "Lehké brnění": {"health": 0, "dexterity": 5, "damage_reduction": 0.1},
            "Střední brnění": {"health": 20, "dexterity": 0, "damage_reduction": 0.2},
            "Těžké brnění": {"health": 40, "dexterity": -5, "damage_reduction": 0.3}
        }
        effects = armor_effects[self.armor]
        self.health += effects["health"]
        self.dexterity += effects["dexterity"]
        self.damage_reduction = effects["damage_reduction"]

    def attack(self):
        damage = random.randint(1, self.strength)
        if random.random() < 0.2:
            damage *= 2
            print(f"Kritický zásah! {self.name} způsobil dvojnásobné poškození.")
        return damage

    def take_damage(self, damage):
        actual_damage = damage * (1 - self.damage_reduction)
        self.health -= actual_damage
        if self.health < 0:
            self.health = 0

    def heal(self, amount):
        self.health += amount
        if self.health > 100:
            self.health = 100

    def use_ability(self, opponent):
        ability, cooldown = self.special_ability
        self.ability_cooldown = cooldown
        self.mana -= 20

        if ability == "Chi výbuch":
            damage = random.randint(10, 30)
            opponent.take_damage(damage)
            self.heal(damage / 2)
            print(f"{self.name} použil {ability} a způsobil {damage:.1f} poškození, vyléčil se za {damage / 2:.1f} zdraví.")
        elif ability == "Přeměna":
            heal_amount = random.randint(10, 30)
            self.heal(heal_amount)
            print(f"{self.name} použil {ability} a vyléčil se za {heal_amount:.1f} zdraví.")
        elif ability == "Elementální bouře":
            damage = random.randint(20, 40)
            opponent.take_damage(damage)
            print(f"{self.name} použil {ability} a způsobil {damage:.1f} poškození.")
        elif ability == "Smrtící výstřel":
            damage = random.randint(15, 35)
            opponent.take_damage(damage)
            print(f"{self.name} použil {ability} a způsobil {damage:.1f} poškození.")
        elif ability == "Rychlý úder":
            damage = random.randint(10, 30)
            opponent.take_damage(damage)
            print(f"{self.name} použil {ability} a způsobil {damage:.1f} poškození.")
        elif ability == "Božský zásah":
            damage = random.randint(20, 40)
            opponent.take_damage(damage)
            self.heal(damage / 2)
            print(f"{self.name} použil {ability} a způsobil {damage:.1f} poškození, vyléčil se za {damage / 2:.1f} zdraví.")

    def regenerate_mana(self):
        self.mana += 5
        if self.mana > 50:
            self.mana = 50

    def decrease_cooldown(self):
        if self.ability_cooldown > 0:
            self.ability_cooldown -= 1

    def __str__(self):
        return f"Gladiátor {self.name}, typ: {self.type}, zdraví: {self.health}, mana: {self.mana}, výzbroj: {self.weapon}, zbroj: {self.armor}"

    def __repr__(self):
        return self.__str__()
