# File Name : EverettFlatch_FinalProject
# Student Name: Rithu Aynampudi
# email: aynampru@mail.uc.edu
# Assignment Number: FinalProject
# Due Date: 05/01/2025
# Course #/Section: IS4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: This assignment decrypts a location, a movie, and upload an image
# Brief Description of what this module does: This module outputs an image taken at the location that is decrypted 
# Citations: RealPython(https://realpython.com/), W3Schools(https://www.w3schools.com/python/)

# imageViewerPackage/image_viewer.py
 
from PIL import Image
import pathlib
 
def show_team_photo(photo_filename="FinalProjEverett.jpg"): 
    ''' 
    This function shows the team image 
    @returns the photo taken in front of the decrypted location
    '''
    base_dir = pathlib.Path(__file__).resolve().parents[1]
    photo_path = base_dir / 'data' / photo_filename
    try:
        img = Image.open(photo_path)
        img.show()
    except FileNotFoundError:
        print(f"[Error] Photo file not found: {photo_path}")
    except Exception as e:
        print(f"[Error] Unable to load photo: {e}")


