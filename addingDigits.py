userinput=input("Enter no: ")
def addingdigits(n):
    tot = 0
    for digit in n:
        tot += int(digit)
    return tot
if __name__ == "__main__":
    print(addingdigits(userinput))
    