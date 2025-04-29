# File Name : fernet_decryptor.py
# Student Name: Jacob Brumfield
# email:  brumfijb@mail.uc.edu
# Assignment Number: Final Project!
# Due Date:   5/1/2025
# Course #/Section:   IS 4010 001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  This assignment decrypts a hidden location and movie.
# Brief Description of what this module does. Decrypts the location of the building that we must take a picture at.
# Citations: 
# Anything else that's relevant:
from cryptography.fernet import Fernet
def decrypt_movie(encrypted_message, key):
    """
    This function decrypts the movie
    Returns: The movie our team was assigned
    """
    try:
        fernet = Fernet(key)
        decrypted = fernet.decrypt(encrypted_message.encode())
        return decrypted.decode()
    except Exception as e:
        return f"[Decryption failed: {e}]"

