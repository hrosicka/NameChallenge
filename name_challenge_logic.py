import requests
import random

class NameChallenge:
    def __init__(self):

        # Initialize variables
        self.correct_answers = 0
        self.total_answers = 0
        # self.names = self.load_names_from_file("names.txt")  # Assuming names.txt exists
        self.names = ["Anna", "Jan", "Tereza", "Martin", "Hana", "Adéla", "Adriana",
                      "Adam", "Alina", "Aleš", "Nicol", "Nikola", "Alex"]  # Example names
    
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

    def check_answer(self, user_answer, name):
        actual_gender = self.get_gender(name)
        if user_answer == actual_gender:
            self.correct_answers += 1
            return "Correct!"
        else:
            self.total_answers += 1
            return f"Incorrect! It was {actual_gender}."
        
    def new_name(self):
        name = random.choice(self.names)
        return name

    def update_stats(self):
        return f"Correct: {self.correct_answers} / {self.total_answers}"