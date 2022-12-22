class Item:
    def __init__(self, name, description, effect, itemtype, results):
        self.name = name
        self.description = description
        self.effect = effect
        self.itemtype = itemtype
        self.results = results

    def offensive_use(self, enemy, inventory, encounter):
        amount = 15
        enemy.take_damage(amount, encounter)
        print(f"You throw the item at the enemy, dealing {amount} damage!")
        inventory.remove_item(self)

    def consume_edible(self, enemy, inventory, encounter):
        if self.itemtype == "Potion":
            empty_container = Item("Empty Bottle",
                                   "This used to hold some sort of liquid. You either found this or drank something and were left with an empty container.",
                                   "Can be refilled. Useful in alchemy and brewing.", "Rations Container",
                                   [Item.offensive_use, Item.print_test_line])

        elif self.itemtype == "Meal":
            empty_container = Item("Empty Meal Container",
                                   "This used to hold some sort of food. You either found this or ate something and were left with an empty container.",
                                   "Can be refilled. Useful in cooking and food storage.", "Rations Container",
                                   [Item.offensive_use])
        else:
            print("Why are you eating this?")
            empty_container = Item("Chewed Up Bits",
                                   "The remains of a brave attempt at eating something that was clearly not meant to be eaten. Covered in your saliva. Off-putting to say the least.",
                                   "Nothing. This is gross. Throw it out as soon as you can.", "Trash",
                                   [Item.offensive_use])
        inventory.add_item(empty_container)
        inventory.remove_item(self)

    def print_test_line(self, enemy, inventory, encounter):
        print(f"Here's {self.name} calling!")
        print(f"I'm over here at the player's inventory.")

    def call_all(self, *args):
        for i in range(0, len(self.results)):
            self.results[i](*args)
