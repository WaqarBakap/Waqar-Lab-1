import os
import time
def pattern_a(rows=9, cols=27):
    for i in range(rows):
        line = ""
        for j in range(cols):
            if (i + j) % 2 == 0:
                line += "\033[42m "  # Green block
            else:
                line += "\033[40m "  # Black block
        print(line + "\033[0m")
if __name__ == '__main__':
    pattern_a()