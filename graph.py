# 3. Function Graph (y = x^2 in 1st quadrant)
def graph_y_x2(height=9, width=20):
    for y in range(height, -1, -1):
        line = ""
        for x in range(width):
            if y == int((x**2) / (width//2)):  # scale
                line += "\033[41m*\033[0m"
            else:
                line += " "
        print(line)
if __name__ == '__main__':
    graph_y_x2()