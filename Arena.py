import random

class Arena:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Arena: {self.name}"

    def apply_random_bonus(self, gladiator):
        if self.name == "Lesní aréna":
            if random.random() < 0.3:
                print(f"{self.name}: Gladiátor {gladiator.name} spadl do pasti v lese -10 zdraví!")
                gladiator.take_damage(10)
        elif self.name == "Pouštní aréna":
            if random.random() < 0.4:
                print(f"{self.name}: Gladiátor {gladiator.name} se zamotala hlava z horka a dostal od soupeře ránu -10 zdraví!")
                gladiator.take_damage(10)
        elif self.name == "Mlžná aréna":
            if random.random() < 0.2:
                print(f"{self.name}: Gladiátor {gladiator.name} nevidí v mlze a narazil -10 zdraví!")
                gladiator.take_damage(10)
        
        # Vypisujeme aktuální zdraví po aplikaci efektu arény
        print(f"{gladiator.name} má nyní {gladiator.health} zdraví.")
