import os
def divisible(x):
    divisible_nums = list()
    for i in range(1, (x+1)):
        if (x % i) == 0:
            divisible_nums.append(i)
    return divisible_nums
# def prime(limit):
def prime(x):
    if divisible(x) == [1, x]:
        ans = str(x) + "\n"
        return ans
    else:
        return ""

with open("primes", "rb") as f:
    f.seek(-2, os.SEEK_END)
    while f.read(1) != b'\n':
        f.seek(-2, os.SEEK_CUR)
    i = int(f.readline().decode()) + 1

while True:
    with open("primes", "a") as f:
        f.write(prime(i))
    i += 1






