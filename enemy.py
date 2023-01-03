import main
from main import *


class Enemy:
    def __init__(self, name, image_file, maxhealth, attack, defense, magic, speed):
        self.name = name
        self.image_file = image_file
        self.health = maxhealth
        self.maxhealth = maxhealth
        self.attack = attack
        self.defense = defense
        self.magic = magic
        self.speed = speed

    def take_damage(self, amount, encounter):
        enemy_defense_mult = 1 - (self.defense/100)
        actual_damage = amount * enemy_defense_mult
        self.health -= amount * enemy_defense_mult
        print(f"{self.name} just took {actual_damage} damage!")
        # Sound
        encounter.health_var.set(self.health)
        playsound(r"sfx\enemyhurt.wav", False)

    def hostile_deal_damage(self, amount):
        print(f"{self.name} just hit you for {amount} damage!!!")