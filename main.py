import reader, game
import os #exists
import ctypes #messagebox
import sys #exit, argv


class Main:
    def __init__(self):
        file = "instructions.txt"
        if len(sys.argv) > 1 and sys.argv[1][-4:] == ".txt":
            file = sys.argv[1]
        if not os.path.exists(file):
            self.error("Cannot find '" + file + "'")
        if not os.path.exists("assets"):
            self.error("Cannot find assets folder")
        
        game.Game(reader.Reader().read(file)).run()
        
    def error(self, message):
        ctypes.windll.user32.MessageBoxW(0, message, "Error", 0)
        sys.exit()

Main()