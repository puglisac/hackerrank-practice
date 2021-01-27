# Write a Python program to check if a given positive integer is a power of two.

def is_pow(num):
    if(num % 2 != 0):
        print("in odd")
        return False
    pow = 1
    while(2 ** pow <= num):
        print(3**2)
        if (2 ** pow == num):
            return True
        pow+=1
    return False

print(is_pow(8))