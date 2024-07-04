import random

class Arena:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Arena: {self.name}"

    def apply_random_bonus(self, gladiator):
        if self.name == "Bahenní aréna":
            if random.random() < 0.3:
                print(f"{self.name}: Gladiátor {gladiator.name} spadl do pasti v bahně -10 zdraví!")
                gladiator.take_damage(10)
            if random.random() < 0.3:
                print(f"{self.name}: Léčivý bahenní kouř uzdravil gladiátora {gladiator.name} +10 zdraví!")
                gladiator.heal(10)
        elif self.name == "Pouštní aréna":
            if random.random() < 0.3:
                print(f"{self.name}: Gladiátor {gladiator.name} se zamotala hlava z horka a dostal od soupeře ránu -10 zdraví!")
                gladiator.take_damage(10)
            if random.random() < 0.3:
                print(f"{self.name}: Oáza uzdravila gladiátora {gladiator.name} +10 zdraví!")
                gladiator.heal(10)
        elif self.name == "Mlžná aréna":
            if random.random() < 0.3:
                print(f"{self.name}: Gladiátor {gladiator.name} nevidí v mlze a narazil -10 zdraví!")
                gladiator.take_damage(10)
            if random.random() < 0.3:
                print(f"{self.name}: Mystické houby uzdravily gladiátora {gladiator.name} +10 zdraví!")
                gladiator.heal(10)
        elif self.name == "Horská aréna":
            if random.random() < 0.3:
                print(f"{self.name}: Gladiátor {gladiator.name} uklouzl na kamenité cestě -10 zdraví!")
                gladiator.take_damage(10)
            if random.random() < 0.3:
                print(f"{self.name}: Horské prameny uzdravily gladiátora {gladiator.name} +10 zdraví!")
                gladiator.heal(10)
        elif self.name == "Ledová aréna":
            if random.random() < 0.3:
                print(f"{self.name}: Gladiátor {gladiator.name} uklouzl na ledu -10 zdraví!")
                gladiator.take_damage(10)
            if random.random() < 0.3:
                print(f"{self.name}: Léčivý led uzdravil gladiátora {gladiator.name} +10 zdraví!")
                gladiator.heal(10)
