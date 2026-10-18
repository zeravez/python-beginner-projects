import os
import pygame

folder = os.path.dirname(os.path.abspath(__file__))
song = os.path.join(folder, "song.mp3")

pygame.mixer.init()
pygame.mixer.music.load(song)

while True:
    print("1. Play")
    print("2. Pause")
    print("3. Resume")
    print("4. Stop and quit")
    choice = input("choose an option: ")
    if choice == "1":
        pygame.mixer.music.play()
    elif choice == "2":
        pygame.mixer.music.pause()
    elif choice == "3":
        pygame.mixer.music.unpause()
    elif choice == "4":
        pygame.mixer.music.stop()
        break