# File Name : decryptor.py
# Student Name: Jacob Brumfield
# email:  brumfijb@mail.uc.edu
# Assignment Number: Final Project
# Due Date:   5/1/2025
# Course #/Section:   IS 4010 001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  This assignment decrypts a hidden location and movie.
# Brief Description of what this module does. Decrypts the location of the building that we must take a picture at.
# Citations: 
# Anything else that's relevant:
def decrypt_location(encrypted_data, word_list):
    """
    This function decrypts the hidden location on campus
    Returns the location
    """
    decrypted_words = []
    for index_str in encrypted_data:
        index = int(index_str)
        if 0 <= index < len(word_list):
            decrypted_words.append(word_list[index])
        else:
            raise IndexError(f"Index {index} out of range.")
    return ' '.join(decrypted_words)


