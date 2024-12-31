import requests
import random

class NameChallenge:
    """
    This class represents the game logic for the name guess challenge.
    It handles retrieving gender information for names using an external API,
    tracking game statistics, and generating new names for the user to guess.
    """

    def __init__(self):
        """
        Initializes the game state variables.

        - correct_answers (int): The number of correctly guessed genders.
        - total_answers (int): The total number of guesses made by the user.
        - names (list): A list of example names used for the game. This can be
          replaced with loading names from a file or another source.
        """

        # Initialize variables
        self.correct_answers = 0
        self.total_answers = 0
        self.names = ["Anna", "Jan", "Tereza", "Martin", "Hana", "Adéla", "Adriana",
                      "Adam", "Alina", "Aleš", "Nicol", "Nikola", "Alex"]  # Example names
    
    def get_gender(self, name):
        """
        Retrieves the gender of a given name using the genderize.io API.

        Args:
            name (str): The name to get the gender for.

        Returns:
            str: The predicted gender ("male" or "female") or None if an error occurs.
        """

        try:
            response = requests.get(f"https://api.genderize.io?name={name}")
            data = response.json()
            return data['gender']
        except requests.exceptions.RequestException as e:
            print(f"Error retrieving gender: {e}")
            return None  # Or display an error message to the user
    
    def get_probability(self, name):
        """
        Retrieves the probability associated with the predicted gender of a name using the genderize.io API.

        Args:
            name (str): The name to get the gender probability for.

        Returns:
            float: The probability value (between 0.0 and 1.0) or None if an error occurs.
        """

        try:
            response = requests.get(f"https://api.genderize.io?name={name}")
            data = response.json()
            return data['probability']
        except requests.exceptions.RequestException as e:
            print(f"Error retrieving gender: {e}")
            return None  # Or display an error message to the user

    def check_answer(self, user_answer, name):
        """
        Checks the user's guess against the actual gender of a name.

        Args:
            user_answer (str): The user's guess for the gender ("male" or "female").
            name (str): The name for which the gender was guessed.

        Returns:
            str: A message indicating the result of the guess (correct or incorrect) and
                 the actual gender of the name.
        """

        actual_gender = self.get_gender(name)
        if user_answer == actual_gender:
            self.correct_answers += 1
            return "Correct!"
        else:
            self.total_answers += 1
            return f"Incorrect! It was {actual_gender}."
        
    def new_name(self):
        """
        Selects a random name from the available name list.

        Returns:
            str: A randomly chosen name from the self.names list.
        """

        name = random.choice(self.names)
        return name

    def update_stats(self):
        """
        Calculates and returns a string representation of the current game statistics.

        Returns:
            str: A formatted string showing the number of correct answers and total guesses.
        """
        
        return f"Correct: {self.correct_answers} / {self.total_answers}"