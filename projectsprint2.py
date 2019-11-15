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

        self.b1 = Button(self, text="Play", command=self.play_music, width=24)
        self.b1.grid(row=1, column=0)

        self.b2 = Button(self, text="Previous", command=self.previous_song,
                         width=18)
        self.b2.grid(row=2, column=0)
        self.b3 = Button(self, text="Toggle", command=self.toggle, width=18)
        self.b3.grid(row=3, column=0)

        self.b4 = Button(self, text="Next", command=self.next_song, width=20)
        self.b4.grid(row=4, column=0)

        self.b5 = Button(self, text="Fav", command=self.add_to_list,
                         width=20)
        self.b5.grid(row=5, column=0)

        self.label1 = Label(self)
        self.label1.grid(row=6, column=0)

        self.output = Text(self, wrap=WORD, width=50)
        self.output.grid(row=8, column=0)

        # set event to not predefined value in pygame
        self.SONG_END = pygame.USEREVENT + 1


        #Opens window to browse data on disk and adds selected songs to play list
        def add_to_list(self):
        
        directory = askopenfilenames()
        # appends song to memory
        for song_dir in directory:
            print(song_dir)
            self.playlist.append(song_dir)
        self.output.delete(0.0, END)

        for key, item in enumerate(self.playlist):
            # appends song to textbox
            song = EasyID3(item)
            song_data = (str(key + 1) + ' : ' + song['title'][0] + ' - '
                         + song['artist'][0])
            self.output.insert(END, song_data + '\n')