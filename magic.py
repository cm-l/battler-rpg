import tk

from main import *


def magic_contents(self):
    self.magic_window = tk.Toplevel(self)
    self.magic_window.title("Magic")
    self.magic_window.geometry("300x240")
    self.magic_window.config(cursor='target')
    tk.Label(self.magic_window, text="Choose a spell to cast")

    # Slot frame
    slots_frame = tk.Frame(self.magic_window)

    # Create the three empty slots
    slot1 = tk.Button(slots_frame, text="1st Phrase")
    slot2 = tk.Button(slots_frame, text="2nd Phrase")
    slot3 = tk.Button(slots_frame, text="3rd Phrase")
    slot4 = tk.Button(slots_frame, text="4th Phrase")
    slot5 = tk.Button(slots_frame, text="Cast Spell")

    instruction = tk.Label(self.magic_window, text="Combine phrases to cast a spell")
    instruction.pack(pady=16)
    slots_frame.pack(side=tk.TOP, anchor=tk.CENTER, pady=16)

    # Arrange the slots in a triangle shape
    slot1.grid(row=0, column=1, pady=8, padx=8)
    slot2.grid(row=1, column=0, pady=8, padx=8)
    slot3.grid(row=1, column=2, pady=8, padx=8)
    slot4.grid(row=2, column=1, padx=8, pady=8)
    slot5.grid(row=1, column=1, pady=10, padx=10)

    spell0 = Spell("Guthri's Favor", 10, tk.PhotoImage(file=r"icons\Icon1.png"), "gha")
    spell1 = Spell("Curse of Mhodhost", 8, tk.PhotoImage(file=r"icons\Icon3.png"), "olpu")
    spell2 = Spell("Yovh'Idrr'Endi's Blessing", 6, tk.PhotoImage(file=r"icons\Icon2.png"), "mox")
    spell3 = Spell("Oshazo's Sermon", 4, tk.PhotoImage(file=r"icons\Icon26.png"), "domeh")
    spell4 = Spell("Acxo'ra'idian Hymn", 2, tk.PhotoImage(file=r"icons\Icon10.png"), "glub")

    spells = [
        spell0,
        spell1,
        spell2,
        spell3,
        spell4
    ]

    casted_result0 = CastedResult("Instant Death", "Kind of self-explainatory.", "I think you can guess.", "moxglubolpumox")
    casted_result1 = CastedResult("Fishification", "Low, yet worrisome risk of misfiring into the caster", "Turns the target into a fish", "glubglubglubglub")

    casted_results = [
        casted_result0,
        casted_result1
    ]

    # Spoken phrase
    spoken_dictionary = {"slot1": "", "slot2": "", "slot3": "", "slot4": ""}

    # Load image
    icon = tk.PhotoImage(file=r"icons\Icon1.png")

    def pick_spell(slot):
        # Create the new window
        spell_window = tk.Toplevel(self.magic_window)

        # Create a listbox for displaying the spells
        listbox = tk.Listbox(spell_window)
        for spell in spells:
            listbox.insert(tk.END, spell.name)

        # Create a button for selecting a spell
        select_button = tk.Button(spell_window, text="Select",
                                  command=lambda: select_spell(slot, listbox.get(tk.ACTIVE)))

        # Arrange the widgets in the window
        listbox.pack()
        select_button.pack()

        # Define a function for selecting a spell and closing the window
        def select_spell(slot, spell_name):
            # Find the selected spell in the list
            selected_spell = None
            for _spell in spells:
                if _spell.name == spell_name:
                    selected_spell = _spell
                    break

            # Update the icon of the slot to show the selected spell
            slot.configure(image=selected_spell.icon)

            # Add phrase to spoken spell
            spoken_dictionary[slot] = selected_spell.phrase

            # Close the window
            spell_window.destroy()

    def speak():
        final_phrase = ""
        final_phrase = spoken_dictionary[slot1] + spoken_dictionary[slot2] + spoken_dictionary[slot3] + spoken_dictionary[slot4]
        print(f"Watch out, here's a spell! {final_phrase.capitalize()}!!!")

        for i in range(0, len(casted_results)):
            if final_phrase == casted_results[i].word:
                print(f"Congrats! You managed to cast {casted_results[i].name}")

        final_phrase = ""
        spoken_dictionary[slot1] = ""
        spoken_dictionary[slot2] = ""
        spoken_dictionary[slot3] = ""
        spoken_dictionary[slot4] = ""

        # Close magic window
        self.magic_window.destroy()



    # Set the command for the three slots to open the spell selection window
    slot1['command'] = lambda: pick_spell(slot1)
    slot2['command'] = lambda: pick_spell(slot2)
    slot3['command'] = lambda: pick_spell(slot3)
    slot4['command'] = lambda: pick_spell(slot4)
    slot5['command'] = lambda: speak()


class Spell:
    def __init__(self, name, mana_cost, icon, phrase):
        self.name = name
        self.mana_cost = mana_cost
        self.icon = icon
        self.phrase = phrase


class CastedResult:
    def __init__(self, name, description, effect, word):
        self.name = name
        self.description = description
        self.effect = effect
        self.word = word
