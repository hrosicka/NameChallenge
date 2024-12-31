from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

import tkinter as tk
import customtkinter
from CTkMessagebox import CTkMessagebox
from tkinter import filedialog

from name_challenge_logic import NameChallenge

class NameChallengeGUI:
    """
    This class represents the graphical user interface (GUI) for the name challenge game.
    It handles creating the main window, displaying game elements, interacting with the game logic,
    and processing user input.
    """

    def __init__(self):
        """
        Initializes the GUI window and its elements.

        - Sets the window title to "Guess the Gender".
        - Disables resizing behavior for a fixed window size.
        - Sets the window geometry to 480x380 pixels.
        - Creates frames to organize the layout of UI elements (work and button frames).
        - Creates a label to display the name for the user to guess.
        - Initializes a string variable to store the user's selected gender ("male", "female", or "none").
        - Creates radio buttons for the user to select the gender ("Male" and "Female").
        - Creates a button with the text "Check" to trigger the answer check.
        - Disables the "Check" button initially until a gender selection is made.
        - Connects the `update_button_state` function to changes in the gender selection variable.
        - Creates labels to display the result of the guess and game statistics.
        - Creates buttons with the text "New name" to generate a new name,
          "Load data from file" to load names from a text file, and
          "Choose file" to open a file dialog for name selection.
        - Starts a new game by calling the `new_name` function.
        - Starts the main event loop of the tkinter application.
        """

        # Create an instance of the game logic
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
                                                    hover_color="#9C4D30")

        self.check_button.pack(pady=10)

        self.check_button.configure(state=tk.DISABLED)

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
                                                        hover_color="#9C4D30")
        self.new_name_button.pack(pady=10)
        
        self.new_data_button = customtkinter.CTkButton(self.button_frame,
                                                        text="Load data from file",
                                                        command=lambda: self.load_names_from_file("names.txt"),
                                                        width=120,
                                                        text_color="white",
                                                        fg_color="#00436C",
                                                        hover_color="#9C4D30")
    
        self.new_data_button.pack(pady=10)


        self.choose_file_button = customtkinter.CTkButton(self.button_frame,
                                                        text="Choose file",
                                                        command=self.choose_file,
                                                        width=120,
                                                        text_color="white",
                                                        fg_color="#00436C",
                                                        hover_color="#9C4D30")
    
        self.choose_file_button.pack(pady=10)

        # Start the game
        self.new_name()
        self.root.mainloop()

    def update_button_state(self):
        """Updates the state of the 'Check' button based on gender selection."""
        if self.gender_var.get() in ["male", "female"]:
            self.check_button.configure(state=tk.NORMAL)
        else:
            self.check_button.configure(state=tk.DISABLED)

    def check_answer(self):
        """Checks if the user guessed the correct gender and updates the result and stats labels."""
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
        """
        Loads names from a specified file.

        Args:
            filename (str): Path to the file containing names.

        Returns:
            list: List of names read from the file, or an empty list if an error occurs.
        """
        try:
            with open(filename, "r") as file:
                names = [line.strip() for line in file]
                self.game.names = names
                return names
        except FileNotFoundError:
            CTkMessagebox(title="Error", message="File not found!!", icon="cancel",
                          width=200,
                          height=150,
                          button_color="#00436C",
                          button_hover_color="#9C4D30",
                          icon_size=(30,30),
                          corner_radius=0,)
            return []
        except Exception as e:
            CTkMessagebox(title="Error", message="An unexpected error occurred!!", icon="cancel",
                          width=200,
                          height=150,
                          button_color="#00436C",
                          button_hover_color="#9C4D30",
                          icon_size=(30,30),
                          corner_radius=0,)
            return []
        
    def choose_file(self):
        """Opens a file dialog for the user to select a file and loads the names from it.

        Handles potential errors during file selection and loading.
        """

        try:
            # Open file dialog and get the selected file path
            file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])

            if file_path:
                # Load names from the file using your existing logic (assuming it's in load_names_from_file)
                names = self.load_names_from_file(file_path)
                self.game.names = names  # Update game names

        except (FileNotFoundError, PermissionError) as e:
            # Handle specific errors like file not found or permission issues
            CTkMessagebox(
                title="Error",
                message=f"An error occurred: {str(e)}",
                icon="cancel",
                width=200,
                height=150,
                button_color="#00436C",
                button_hover_color="#9C4D30",
                icon_size=(30, 30),
                corner_radius=0,
            )

        except Exception as e:
            # Catch any other unexpected errors
            CTkMessagebox(
                title="Error",
                message="An unexpected error occurred!",
                icon="cancel",
                width=200,
                height=150,
                button_color="#00436C",
                button_hover_color="#9C4D30",
                icon_size=(30, 30),
                corner_radius=0,
            )


# Create an instance of the game
game = NameChallengeGUI()