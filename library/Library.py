import sys
import os
import curses
import curses.textpad
from excepts.CLI_Audio_Exception import CLI_Audio_File_Exception

class Library:
    
    def __init__(self):
        self.stdscr = curses.initscr()
        self.files = []
        self.playlist = []
        
        
    def findLibrary(self):
        changeWindow = curses.newwin(5, 40, 15, 50) #hieght, width, y, x
        changeWindow.border()
        changeWindow.addstr(0,0, "What is the directory?", curses.A_REVERSE)
        changeWindow.addstr(1,0, "EX: type 'media' if directory", curses.A_REVERSE)
        curses.echo()
        path = changeWindow.getstr(2,1, 30)
        curses.noecho()
        self.getFiles(path)


    def getFiles(self,path):
        try:
            if not os.path.exists(path):
                raise CLI_Audio_File_Exception
            
        except CLI_Audio_File_Exception:
            self.stdscr.addstr(17, 10, "ERROR: Invalid Directory")
            return
        
        self.stdscr.addstr(17, 10, "                        ")
        music = os.listdir(path)
        for file in music:
                self.files.append(file)
            
        
    def addPlaylist(self):
        changeWindow = curses.newwin(5, 40, 15, 50)
        changeWindow.border()
        changeWindow.addstr(0,0, "What song do you want to play?", curses.A_REVERSE)
        curses.echo()
        song = changeWindow.getstr(1,1, 30)
        
        try:
            if song in self.files:
                self.stdscr.addstr(17, 10, "                             ")
                self.playlist.append(song)
            else:
                 raise CLI_Audio_File_Exception
            
        except CLI_Audio_File_Exception:
            self.stdscr.addstr(17, 10, "ERROR: Invalid Song Request")
        

    