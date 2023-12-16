"""
Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
"""
import os
import pygame

pygame.init()                                                   # Initialize Pygame
pygame.mixer.init()                                             # Initialize the Pygame audio mixer

MP3_FILE_NAME = 'ex021.mp3'                                     # Name of the music file
SCRIPT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))   # Path to the directory where the script is located
MP3_FILE_PATH = os.path.join(SCRIPT_DIRECTORY, MP3_FILE_NAME)   # Full path to the MP3 file using os.path.join

pygame.mixer.music.load(MP3_FILE_PATH)                          # Load the MP3 file
pygame.mixer.music.play()                                       # Play the MP3 file

while pygame.mixer.music.get_busy():                            # Keep the program running while the music is playing
    pygame.time.Clock().tick(10)                                # Control the refresh rate to avoid excessive CPU usage

pygame.quit()                                                   # Quit Pygame
