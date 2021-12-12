import os #exists
import sys #exit 
import ctypes #messagebox 


class Reader:
    def read(self, file):
        lines = open(file).readlines()
        #["background:picture.png\n", "text:writing\n"]
        
        new_lines = []
        for number, line in enumerate(lines):
            if line.strip() == "":
                new_lines.append("empty")
            else:
                if ":" in line:
                    split = line.split(":")
                    new_lines.append([split[0].strip(), split[1].strip()])
                else:
                    self.error("[Line {}] Missing colon".format(number + 1))
        #[["background", "picture.png"], ["text", "writing"]]
        #chunks instructions, removes whitespace
            
        for number, line in enumerate(new_lines):
            if line == "empty": #blank lines are represented by "empty"
                pass 
                
            elif line[0] == "comment":
                pass 
                
            elif line[0] == "background":
                if line[1] == "":
                    self.error("[Line {}] 'background' instruction missing image name".format(number + 1))
                elif os.path.exists("assets\\" + line[1]) == False:
                    self.error("[Line {}] Cannot find '{}' in assets folder".format(number + 1, line[1]))
                elif not line[1][-4:] == ".png" and not line[1][-4:] == ".jpg":
                    self.error("[Line {}] Only png and jpg images are supported".format(number + 1))
                    
            elif line[0] == "text":
                if len(line[1]) > 120:
                    self.error("[Line {}] Text cannot exceed 120 characters".format(number + 1)) #----------------------------------------------
                
            elif line[0] == "options":
                if len(line[1]) == 0:
                    self.error("[Line {}] 'options' instruction has no options".format(number + 1))
                elif self.next_instruction(new_lines, number)[0] != "answer":
                    self.error("[Line {}] 'answer' instruction must come after 'options' instruction".format(number + 1))
                elif line[1].count(" ") > 3:
                    self.error("[Line {}] Maximum 4 options".format(number + 1))
                else:
                    split = line[1].split(" ")
                    for number2, option in enumerate(split):
                        if len(option) > 10:
                            self.error("[Line {}] Option {} cannot exceed 10 characters".format(number + 1, number2 + 1)) #-----------------------
                    
            elif line[0] == "answer":
                last_instruction = self.last_instruction(new_lines, number)
                if last_instruction[0] != "options":
                    self.error("[Line {}] 'options' instruction must come before 'answer' instruction".format(number + 1))
                else:
                    options = last_instruction[1].split(" ")
                    found = False
                    for option in options:
                        if option == line[1]:
                            found = True
                            break
                    if found == False:
                        self.error("[Line {}] Answer must be a given option".format(number + 1))
                
            else:
                self.error("[Line {}] Unknown instruction".format(number + 1))
            
        return new_lines
                
    def last_instruction(self, lines, index):
        while (index > 0):
            index -= 1
            if lines[index] != "empty":
                return lines[index]
        return "empty"
                
    def next_instruction(self, lines, index):
        while (index < len(lines) - 1):
            index += 1
            if lines[index] != "empty":
                return lines[index]
        return "empty"
    
    def check_empty(self, lines):
        if len(lines) == 0:
            return True
        else:
            for line in lines:
                if line != "empty":
                    return False
            return True
            
    def error(self, error):
        ctypes.windll.user32.MessageBoxW(0, error, "Error", 0)
        sys.exit()
