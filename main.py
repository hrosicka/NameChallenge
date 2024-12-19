from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

import tkinter as tk
import requests
import random

class NameChallenge:
    def __init__(self):
        # Initialize variables
        self.correct_answers = 0
        self.total_answers = 0
        self.names = ["Anna", "Jan", "Tereza", "Martin", "Hana", "Adéla", "Adriana",
                      "Adam", "Alina", "Aleš", "Nicol", "Nikola", "Alex"]  # Example names

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

    def get_gender(self, name):
        """Gets the gender of a name using the genderize.io API."""
        try:
            response = requests.get(f"https://api.genderize.io?name={name}")
            data = response.json()
            return data['gender']
        except requests.exceptions.RequestException as e:
            print(f"Error retrieving gender: {e}")
            return None  # Or display an error message to the user
    
    def get_probability(self, name):
        """Gets the probability of a name using the genderize.io API."""
        try:
            response = requests.get(f"https://api.genderize.io?name={name}")
            data = response.json()
            return data['probability']
        except requests.exceptions.RequestException as e:
            print(f"Error retrieving gender: {e}")
            return None  # Or display an error message to the user

    def check_answer(self):
        """Checks if the user guessed the correct gender."""
        user_answer = self.gender_var.get()
        actual_gender = self.get_gender(self.name_label['text'])
        if user_answer == actual_gender:
            self.result_label['text'] = "Correct!"
            self.correct_answers += 1
        else:
            self.result_label['text'] = f"Incorrect! It was {actual_gender}."
            self.total_answers += 1
        self.update_stats()

    def new_name(self):
        """Generates a new random name and updates the GUI."""
        name = random.choice(self.names)
        self.name_label['text'] = name
        self.gender_var.set("none")

    def update_stats(self):
        """Updates the success statistics."""
        self.stats_label['text'] = f"Correct: {self.correct_answers} / {self.total_answers}"

# Create an instance of the game
game = NameChallenge()