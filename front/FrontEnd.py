import curses
import curses.textpad
import sys
import os
from excepts.CLI_Audio_Exception import CLI_Audio_Screen_Size_Exception
from excepts.CLI_Audio_Exception import CLI_Audio_File_Exception

class FrontEnd:

    def __init__(self, player,library):
        self.stdscr = curses.initscr()
        self.height, self.width = self.stdscr.getmaxyx()
        try:
            if (self.height < 30):
                raise CLI_Audio_Screen_Size_Exception
            if (self.width < 100):
                raise CLI_Audio_Screen_Size_Exception
        except CLI_Audio_Screen_Size_Exception:
            print("ERROR: Screen size is too small to run program")
            exit()
        self.player = player
        self.library = library
        #self.player.play("media/UptownFunk.wav")
        curses.wrapper(self.menu)

    def menu(self, args):
        self.stdscr = curses.initscr()
        self.stdscr.border()
        self.stdscr.addstr(0,0, "cli-audio",curses.A_REVERSE)
        self.stdscr.addstr(5,10, "c - Change current song")
        self.stdscr.addstr(6,10, "p - Play/Pause")
        self.stdscr.addstr(7,10, "l - Library")
        self.stdscr.addstr(8,10, "a - add to playlist")
        self.stdscr.addstr(10,10, "ESC - Quit")
        self.updateSong()
        self.stdscr.refresh()
        while True:
            c = self.stdscr.getch()
            if c == 27:
                self.quit()
            elif c == ord('p'):
                if self.player.currentSong == "Nothing playing.":
                    self.stdscr.addstr(17, 10, "ERROR: Choose Library First")
                else:
                    self.player.pause()
                self.stdscr.touchwin()
                self.stdscr.refresh()    
            elif c == ord('c'):
                self.changeSong()
                self.updateSong()
                self.stdscr.touchwin()
                self.stdscr.refresh()
            elif c == ord('l'):
                self.stdscr.addstr(17, 10, "                               ")
                self.library.findLibrary()
                self.displayLibrary()
                self.stdscr.touchwin()
                self.stdscr.refresh()
            elif c == ord('a'):
                self.library.addPlaylist()
                self.displayPlaylist()
                self.updateSong()
                self.stdscr.touchwin()
                self.stdscr.refresh()
        
    
    def updateSong(self):
        self.stdscr.addstr(15,10, "                                        ")
        self.stdscr.addstr(15,10, "Now playing: " + self.player.getCurrentSong())

    def changeSong(self):
        changeWindow = curses.newwin(5, 40, 15, 50) #hieght, width, y, x
        changeWindow.border()
        changeWindow.addstr(0,0, "What is the file path?", curses.A_REVERSE)
        self.stdscr.refresh()
        curses.echo()
        path = changeWindow.getstr(1,1, 30)
        curses.noecho()
        del changeWindow
        self.stdscr.touchwin()
        self.stdscr.refresh()
        if self.player.currentSong == "Nothing playing.":
            self.stdscr.addstr(17, 10, "ERROR: Choose Library First")
            return
        self.player.stop()
        try:
            
            self.player.play(path.decode(encoding="utf-8"))
            self.stdscr.addstr(17, 10, "                   ")
        except CLI_Audio_File_Exception:
            self.stdscr.addstr(17, 10, "ERROR: Invalid Path")
            
    
    def displayLibrary(self):
        if not self.library.files:
            self.stdscr.addstr(5, 50, "Library: Empty")
        else:
            self.stdscr.addstr(5, 50, "Library:")
            x = 1
            for song in self.library.files:
                self.stdscr.addstr(5 + x,50, str(x) + ": " + song)
                x = x + 1
      
    
    def displayPlaylist(self):
        if not self.library.playlist:
            self.stdscr.addstr(5, 75, "Playlist: Empty")
        else:
            self.stdscr.addstr(5, 75, "Playlist:")
            i = 1
            for soundtrack in self.library.playlist:
                self.player.play("media/" + soundtrack)
                self.stdscr.addstr(5 + i, 75, str(i) + ": " + soundtrack)
                i = i + 1
            
    
    def quit(self):
        self.player.stop()
        exit()