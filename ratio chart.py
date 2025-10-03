

def ratio_chart(filename="sequence.txt"):
    with open(filename, "r") as f:
        numbers = list(map(float, f.read().split()))

    less_than_zero = sum(1 for n in numbers if n < 0)
    greater_than_zero = sum(1 for n in numbers if n > 0)
    total = less_than_zero + greater_than_zero

    less_percent = (less_than_zero / total) * 100 if total else 0
    greater_percent = (greater_than_zero / total) * 100 if total else 0

    print("Numbers < 0 : " + "█" * int(less_percent//2) + f" {less_percent:.1f}%")
    print("Numbers > 0 : " + "█" * int(greater_percent//2) + f" {greater_percent:.1f}%")
    
    
if __name__ == '__main__':
    ratio_chart()