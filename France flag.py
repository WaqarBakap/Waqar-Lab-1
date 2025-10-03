

def france_flag(height=9, width=27):
    for _ in range(height):
        print("\x1b[44m" + " " * (width//3) +  
              "\x1b[47m" + " " * (width//3) +  
              "\x1b[41m" + " " * (width//3) + 
              "\x1b[0m")
        
        
if __name__ == '__main__':
    france_flag()