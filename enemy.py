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
        self.health -= amount
        print(f"{self.name} just took {amount} damage!")
        encounter.health_var.set(self.health)

    def hostile_deal_damage(self, amount):
        print(f"{self.name} just hit you for {amount} damage!!!")