# File Name : EverettFlatch_FinalProject
# Student Name: Sharvari Patil, Rithu Aynampudi, Jacob Brumfield
# email: aynampru@mail.uc.edu
# Assignment Number: FinalProject
# Due Date: 05/01/2025
# Course #/Section: IS4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: This assignment decrypts a location, a movie, and upload an image
# Brief Description of what this module does: This module outputs an image taken at the location that is decrypted 
# Citations: RealPython(https://realpython.com/), W3Schools(https://www.w3schools.com/python/)
 
import pathlib
import json
 
from mainPackage import file_loader
from decryptorPackage import decryptor, fernet_decryptor
from imageViewerPackage import image_viewer
 
def main():
    base_dir = pathlib.Path(__file__).resolve().parents[1]
 
    # Load original location data
    english_file_path = base_dir / 'data' / 'UCEnglish.txt'
    encrypted_json_path = base_dir / 'data' / 'EncryptedGroupHints Spring 2025.json'
    word_list = file_loader.load_word_list(english_file_path)
    encrypted_data = file_loader.load_encrypted_json(encrypted_json_path)
 
    # Decrypt location
    team_name = "Everett Flatch"
    if team_name in encrypted_data:
        encrypted_indices = encrypted_data[team_name]
        location = decryptor.decrypt_location(encrypted_indices, word_list)
    else:
        location = "Location not found."
 
    # Decrypt encrypted movie title
    encrypted_movie_file = base_dir / 'data' / 'TeamsAndEncryptedMessagesForDistribution.json'
    with open(encrypted_movie_file, 'r', encoding='utf-8') as f:
        encrypted_movies = json.load(f)
 
    if team_name in encrypted_movies:
        encrypted_message = encrypted_movies[team_name][0]  # Extract the first message
        fernet_key = b'psY03QLeJfiaxs-jC8wSEQO-sUHbJW7moCiMH_FnBdQ='  # Instructor's key
        decrypted_movie = fernet_decryptor.decrypt_movie(encrypted_message, fernet_key)
    else:
        decrypted_movie = "Movie title not found."
 
    # Output results
    print(f"Location: {location}")
    print(f"Movie Title: {decrypted_movie}")
 
    # Display the team photo
    image_viewer.show_team_photo("FinalProjEverett.jpg")  # Ensure this file exists in /data
 
if __name__ == '__main__':
    main()
