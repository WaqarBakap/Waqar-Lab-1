import os
import time


def france_flag(height=9, width=27):
    for _ in range(height):
        print("\x1b[44m" + " " * (width//3) +   # Blue
              "\x1b[47m" + " " * (width//3) +   # White
              "\x1b[41m" + " " * (width//3) +   # Red
              "\x1b[0m")
        

def pattern_a(rows=9, cols=27):
    for i in range(rows):
        line = ""
        for j in range(cols):
            if (i + j) % 2 == 0:
                line += "\x1b[42m " 
            else:
                line += "\x1b[40m " 
        print(line + "\x1b[0m")


def animation():
    for _ in range(5):
        os.system("cls" if os.name == "nt" else "clear")
        france_flag(6, 18)
        time.sleep(0.5)
        os.system("cls" if os.name == "nt" else "clear")
        pattern_a(6, 18)
        time.sleep(0.5)


if __name__ == '__main__':
    animation()