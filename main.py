from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

import tkinter as tk


from name_challenge_logic import NameChallenge

class NameChallengeGUI:
    def __init__(self):

        self.game = NameChallenge()

        # Create the main window
        self.root = tk.Tk()
        self.root.title("Guess the Gender")

        # Create GUI elements
        self.name_label = tk.Label(self.root, text="...", font=("Arial", 16))
        self.name_label.pack(pady=20)

        self.gender_var = tk.StringVar()
        self.gender_var.set("none")

        self.male_button = tk.Radiobutton(self.root, text="Male", variable=self.gender_var, value="male")
        self.male_button.pack()
        self.female_button = tk.Radiobutton(self.root, text="Female", variable=self.gender_var, value="female")
        self.female_button.pack()

        self.check_button = tk.Button(self.root, text="Check", command=self.check_answer)
        self.check_button.pack(pady=10)

        # Inicializace stavu tlačítka
        self.check_button.config(state=tk.DISABLED)

        # Připojení funkce k proměnné gender_var
        self.gender_var.trace_add("write", lambda *args: self.update_button_state())

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

        self.stats_label = tk.Label(self.root, text="")
        self.stats_label.pack()

        self.new_name_button = tk.Button(self.root, text="New Name", command=self.new_name)
        self.new_name_button.pack()

        # Start the game
        self.new_name()
        self.root.mainloop()


    # Funkce pro aktualizaci stavu tlačítka
    def update_button_state(self):
        if self.gender_var.get() in ["male", "female"]:
            self.check_button.config(state=tk.NORMAL)
        else:
            self.check_button.config(state=tk.DISABLED)

    def check_answer(self):
        """Checks if the user guessed the correct gender."""
        user_answer = self.gender_var.get()
        name = self.name_label['text']
        result = self.game.check_answer(user_answer, name)
        self.result_label["text"] = result
        self.game.update_stats()
        # Update stats label

    def new_name(self):
        """Generates a new random name and updates the GUI."""
        name = self.game.new_name()
        self.name_label['text'] = name
        self.gender_var.set("none")


    def load_names_from_file(self, filename):
        try:
            with open(filename, "r") as file:
                names = [line.strip() for line in file]
            return names
        except FileNotFoundError:
            print(f"Error loading names file: {filename}")
            return []

# Create an instance of the game
game = NameChallengeGUI()