#import for Metadata, GUI, and Music Player

from mutagen.easyid3 import EasyID3
import pygame
from tkinter.filedialog import *
from tkinter import *

pygame.init()

#create GUI buttons
class FrameApp(Frame):
    def __init__(self,master):
        super(FrameApp, self).__init__(master)

        self.grid()
        self.paused = False
        self.playlist = list()
        self.actual_song = 0

        self.b1 = Button(self, text="play", command=self.play_music, width=20)
        self.b1.grid(row=1, column=0)

        self.b2 = Button(self, text="previous", command=self.previous_song,
                         width=20)
        self.b2.grid(row=2, column=0)
