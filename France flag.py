
import os
import time

# 1. FLAG of France (3 vertical stripes: Blue, White, Red)
def france_flag(height=9, width=27):
    for _ in range(height):
        print("\x1b[44m" + " " * (width//3) +   # Blue
              "\x1b[49m" + " " * (width//3) +   # White
              "\x1b[41m" + " " * (width//3) +   # Red
              "\x1b[0m")
if __name__ == '__main__':
    france_flag()