# File Name : EverettFlatch_FinalProject
# Student Name: SHarvari Patil, Rithu Aynampudi, Jacob Brumfield
# email: aynampru@mail.uc.edu
# Assignment Number: FinalProject
# Due Date: 05/01/2025
# Course #/Section: IS4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: This assignment decrypts a location, a movie, and upload an image
# Brief Description of what this module does: This module outputs an image taken at the location that is decrypted 
# Citations: RealPython(https://realpython.com/), W3Schools(https://www.w3schools.com/python/)

def load_word_list(file_path):
    """
    Load a list of words from a text file.

    Each line in the file is expected to contain one word.
    Leading and trailing whitespace is stripped from each line.

    Returns:
        list of str: A list of words from the file.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file]


def load_encrypted_json(file_path):
    """
    Load and parse a JSON file containing encrypted data.

    The function reads the file and deserializes its contents into
    a Python dictionary or list, depending on the JSON structure.

    Returns:
        dict or list: The parsed JSON data.
    """
    import json
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)
