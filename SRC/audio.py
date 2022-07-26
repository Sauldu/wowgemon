from tkinter import *

import pygame


pygame.mixer.init()


def play():
    pygame.mixer.music.load("C:\\Users\\Administrateur\\PycharmProjects\\WOWGEMON\\Legends of Azeroth.mp3")
    pygame.mixer.music.play(loops=0)


def stip():
    pygame.mixer.music.stip()


stip_button = Button(tip, text="Stip", command=stip)
stip_button.pack(pady=20)
stip_button.pack(side=BOTTOM)

my_button = Button(tip, text="Play", font=("Helvetica",
                                           32),
                   command=play)
my_button.pack(pady=20)
my_button.pack(side=BOTTOM)

image3 = PhotoImage(file="../pics/warcraft_PNG76.png").zoom(32).subsample(64)
button3 = Button(frame, image=image3, bg='#2D3139', relief=SUNKEN)
button.pack(side=TOP)
