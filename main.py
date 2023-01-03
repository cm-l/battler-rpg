import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from playsound import playsound

from enemy import *
from item import *
from inventory import *


class BattleEncounter(tk.Tk):
    def __init__(self, enemy, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Initialize class variables to store the open windows
        self.attack_window = None
        self.defend_window = None
        self.magic_window = None
        self.item_window = None

        self.title("RPG Battle Encounter")
        self.geometry("640x480")

        # Create a main frame to hold everything
        main_frame = tk.Frame(self, padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Add enemy name
        tk.Label(main_frame, text=enemy.name, font=("Helvetica", 16)).pack(pady=10)

        # Load the enemy image using PIL
        enemy_image = Image.open(enemy.image_file)
        enemy_image = enemy_image.resize((260, 260))
        self.enemy_image = ImageTk.PhotoImage(enemy_image)

        # Add enemy image with grooved border and fixed size
        image_frame = tk.Frame(main_frame, bd=3, relief=tk.GROOVE)
        image_label = tk.Label(image_frame, image=self.enemy_image, width=260, height=260)
        image_label.pack()
        image_frame.pack()

        # Add enemy health bar
        self.health_var = tk.IntVar()
        self.health_bar = ttk.Progressbar(main_frame, variable=self.health_var, maximum=100)
        self.health_bar.pack()

        # Set the initial value of the health bar
        self.health_var.set(enemy.health)

        # Create a frame to hold the buttons
        button_frame = tk.Frame(main_frame, bd=2, relief=tk.GROOVE)

        # Add attack button
        tk.Button(button_frame, text="Attack", command=self.attack).grid(row=0, column=0, padx=10, pady=10)

        # Add defend button
        tk.Button(button_frame, text="Defend", command=self.defend).grid(row=0, column=1, padx=10, pady=10)

        # Add magic button
        tk.Button(button_frame, text="Magic", command=self.magic).grid(row=1, column=0, padx=10, pady=10)

        # Add item button
        tk.Button(button_frame, text="Item", command=self.item).grid(row=1, column=1, padx=10, pady=10)

        # Pack the button frame
        button_frame.pack()

        # Create a main menu
        menu = tk.Menu(self)
        self.config(menu=menu)

        # Create a File menu
        file_menu = tk.Menu(menu)
        menu.add_cascade(label="Actions and Settings", menu=file_menu)
        file_menu.add_command(label="Exit", command=self.quit)

    # Populate player inventory
    # Create an instance of the Item class
    item1 = Item("Potion",
                 "Small and sturdy flask. It's warm to the touch and filled to the brim with a viscous, thick, red liquid.",
                 "Restores a respectable amount of health.", "Potion", [Item.consume_edible])
    item2 = Item("Ether",
                 "A glass bottle, unusually light for its size. Filled with a mysterious, transparent substance.",
                 "Restores a small amount of mana.", "Potion", [Item.consume_edible])
    item3 = Item("Magnifying Lens",
                 "A lens the size of a fingernail, used to make small objects appear larger. It's cracked and dirty. Imbued with magical energy.",
                 "Gives you insight on the enemy you've encountered.", "Artifact", [Item.print_test_line])
    item4 = Item("Seltzer",
                 "A fancy bottle, adorned with ridged patterns and a colorful label. Contains slightly carbonized water.",
                 "Not much. Makes your tongue feel numb for a moment.", "Potion", [Item.consume_edible])

    item5 = Item("Sharp Debree",
                 "A broken piece of an unknown object with edges sharp enough to cut through skin.",
                 "Can be thrown for minor damage.", "Offensive Item", [Item.offensive_use])

    # Create an instance of the Inventory class
    inventory = Inventory()

    # Add the items to the inventory
    inventory.add_item(item1)
    inventory.add_item(item2)
    inventory.add_item(item3)
    inventory.add_item(item5)

    # Add a lot of potions
    for _ in range(0, 7):
        inventory.add_item(item5)

    def attack(self):
        # Open a new window for the attack action if it is not already open
        if not self.attack_window:
            self.attack_window = tk.Toplevel(self)
            self.attack_window.title("Attack")
            self.attack_window.geometry("300x300")
            tk.Label(self.attack_window, text="Perform offensive action").pack()

            # Bind the <Destroy> event to the window and set the class variable to None in the event handler
            self.attack_window.bind("<Destroy>", lambda event: setattr(self, "attack_window", None))
        else:
            self.attack_window.focus_force()

    def defend(self):
        # Open a new window for the defend action if it is not already open
        if not self.defend_window:
            self.defend_window = tk.Toplevel(self)
            self.defend_window.title("Defend")
            self.defend_window.geometry("300x300")
            tk.Label(self.defend_window, text="Perform defensive action").pack()

            # Bind the <Destroy> event to the window and set the class variable to None in the event handler
            self.defend_window.bind("<Destroy>", lambda event: setattr(self, "defend_window", None))
        else:
            self.defend_window.focus_force()

    def magic(self):
        # Open a new window for the magic action if it is not already open
        if not self.magic_window:
            self.magic_window = tk.Toplevel(self)
            self.magic_window.title("Magic")
            self.magic_window.geometry("300x300")
            tk.Label(self.magic_window, text="Choose a spell to cast").pack()

            # Bind the <Destroy> event to the window and set the class variable to None in the event handler
            self.magic_window.bind("<Destroy>", lambda event: setattr(self, "magic_window", None))
        else:
            self.magic_window.focus_force()

    def item(self):
        # Open a new window for the item action if it is not already open
        if not self.item_window:
            self.item_window = tk.Toplevel(self)
            self.item_window.title("Item")
            self.item_window.geometry("480x640")
            tk.Label(self.item_window, text="Select an item").pack()

            # Items frame
            # Create a frame to hold the listbox and text widget
            item_frame = tk.Frame(self.item_window, padx=10, pady=10)
            item_frame.pack(fill=tk.BOTH, expand=True)

            # Create the listbox to display the names of the items
            item_list = tk.Listbox(item_frame, width=28)
            item_list.pack(side=tk.LEFT, fill=tk.BOTH)

            # Create the label widget to display the description of the selected item
            item_label1 = tk.Label(item_frame, height=10, width=320, anchor=tk.NW, justify=tk.LEFT, wraplength=262,
                                   padx=6, pady=6, relief=tk.RIDGE)
            item_label1.pack(side=tk.RIGHT, fill=tk.BOTH, expand=False)
            # Create the label widget to display effect of selected item
            item_label2 = tk.Label(item_frame, width=10, height=35, anchor=tk.NW, justify=tk.LEFT, relief=tk.RIDGE)
            item_label2.pack(side=tk.BOTTOM, anchor=tk.S, fill=tk.BOTH, expand=False)

            # Create the "Use Item" button
            use_button = tk.Button(self.item_window, text="Use Item", relief=tk.RAISED, pady=2)
            use_button.pack(side=tk.BOTTOM, pady=8)

            # Populate the listbox with the names of the items
            for item in self.inventory.items:
                item_list.insert(tk.END, item.name)

                # Define a function to display the description of the selected item
                def show_description(event):
                    index = item_list.curselection()[0]
                    currentitem = self.inventory.items[index]
                    # Use result
                    # TODO make it so that it uses ALL the functions of the item instead of just "Eat/drink the item"
                    # TODO make it so that the current item's results can take a varying number of arguments (*kwargs, args, **kwargs, etc)
                    # use_button.config(command=lambda: [currentitem.results[0](currentitem, self.inventory), self.item_window.destroy(), self.item()])
                    args_dict = {"enemy": myenemy, "inventory": self.inventory, "encounter": app}
                    use_button.config(
                        command=lambda: [currentitem.call_all(currentitem, myenemy, self.inventory, app),
                                         self.item_window.destroy(),
                                         self.item()])
                    item_label1.config(
                        text=f"I. NAME\n{currentitem.name}\n\nII. DESCRIPTION\n{currentitem.description}\n\nIII. EFFECTS\n{currentitem.effect}\n\nIV. TYPE OF ITEM\n{currentitem.itemtype}")

                # Bind the function to the listbox
                item_list.bind("<<ListboxSelect>>", show_description)

            # Bind the <Destroy> event to the window and set the class variable to None in the event handler
            self.item_window.bind("<Destroy>", lambda event: setattr(self, "item_window", None))
        else:
            self.item_window.focus_force()


if __name__ == "__main__":
    # Create an instance of the Enemy class
    myenemy = Enemy("Goblin", "enemy.png", 100, 50, 15, 30, 70)

    # Create an instance of the BattleEncounter class and pass the enemy instance
    app = BattleEncounter(myenemy)
    app.mainloop()
