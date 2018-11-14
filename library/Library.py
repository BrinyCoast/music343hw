import sys
import os

class Library:
    def check(self):
        path = changeWindow.getstr(1,1, 30) + '.wav'
        exist = os.path.isfile('/media/' + path)
        if exist:
            addfiles(path)
        else:
            self.stdscr.addstr(9,10, "Path does not exist")


    def addFile(path):
        file = open("library.txt", "w")
        file.write(path)
        player.play(file)



