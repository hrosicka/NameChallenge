from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

import tkinter as tk
import customtkinter


from name_challenge_logic import NameChallenge

class NameChallengeGUI:
    def __init__(self):

        self.game = NameChallenge()

        # Create the main window
        self.root = tk.Tk()
        self.root.title("Guess the Gender")

        self.root.resizable(False, False) 
        self.root.geometry("480x380")

        self.work_frame = tk.Frame(self.root)
        self.work_frame.pack(side=tk.LEFT, padx=40, pady=20)

        # Create a frame to hold the buttons
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(side=tk.RIGHT, padx=20, pady=20)

        # Create GUI elements
        self.name_label = tk.Label(self.work_frame, text="...", font=("Arial", 16))
        self.name_label.pack(pady=20)

        self.gender_var = tk.StringVar()
        self.gender_var.set("none")

        self.male_button = customtkinter.CTkRadioButton(self.work_frame,
                                                        text="Male",
                                                        radiobutton_width=20,
                                                        radiobutton_height=20,
                                                        border_width_checked=6,
                                                        hover_color="#9C4D30",
                                                        fg_color="#00436C",
                                                        variable=self.gender_var,
                                                        value="male")
        self.male_button.pack()
        self.female_button = customtkinter.CTkRadioButton(self.work_frame, 
                                                          text="Female",
                                                          radiobutton_width=20,
                                                          radiobutton_height=20,
                                                          border_width_checked=6,
                                                          hover_color="#9C4D30",
                                                          fg_color="#00436C",
                                                          variable=self.gender_var,
                                                          value="female")
        self.female_button.pack()


        self.check_button = customtkinter.CTkButton(self.button_frame,
                                                    text="Check",
                                                    command=self.check_answer,
                                                    width=120,
                                                    text_color="white",
                                                    fg_color="#00436C",
                                                    hover_color="#9C4D30",
                                                    corner_radius=0)

        self.check_button.pack(pady=10)

        # Inicializace stavu tlačítka
        self.check_button.configure(state=tk.DISABLED)

        # Připojení funkce k proměnné gender_var
        self.gender_var.trace_add("write", lambda *args: self.update_button_state())

        self.result_label = tk.Label(self.work_frame, text="")
        self.result_label.pack()

        self.stats_label = tk.Label(self.work_frame, text="")
        self.stats_label.pack()

        self.new_name_button = customtkinter.CTkButton(self.button_frame,
                                                        text="New name",
                                                        command=self.new_name,
                                                        width=120,
                                                        text_color="white",
                                                        fg_color="#00436C",
                                                        hover_color="#9C4D30",
                                                        corner_radius=0)
        self.new_name_button.pack(pady=10)
        
        self.new_data_button = customtkinter.CTkButton(self.button_frame,
                                                        text="Load data from file",
                                                        command=self.new_name,
                                                        width=120,
                                                        text_color="white",
                                                        fg_color="#00436C",
                                                        hover_color="#9C4D30",
                                                        corner_radius=0)
    
        self.new_data_button.pack(pady=10)

        # Start the game
        self.new_name()
        self.root.mainloop()


    # Funkce pro aktualizaci stavu tlačítka
    def update_button_state(self):
        if self.gender_var.get() in ["male", "female"]:
            self.check_button.configure(state=tk.NORMAL)
        else:
            self.check_button.configure(state=tk.DISABLED)

    def check_answer(self):
        """Checks if the user guessed the correct gender."""
        user_answer = self.gender_var.get()
        name = self.name_label['text']
        result = self.game.check_answer(user_answer, name)
        self.result_label["text"] = result
        stat = self.game.update_stats()
        self.stats_label["text"] = stat

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