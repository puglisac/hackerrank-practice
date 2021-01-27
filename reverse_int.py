def reverse_int(n):     
    """given an integer, return digits of integer in reversed order
        if reversed integer >2^31-1 or <-2^31, return 0

        >>> reverse_int(123)
        321

        >>> reverse_int(2**32)
        0

        >>> reverse_int(-56734)
        -43765

    """
    neg=n<0 
    int_arr = [char for char in str(abs(n))]
    reversed_array=[]
    reversed_n=None

    for i in range(len(int_arr)-1, -1, -1):
        reversed_array.append(int_arr[i])

    if(neg):
        reversed_n = int("".join(reversed_array)) * -1
    else:
        reversed_n = int("".join(reversed_array))

    if(reversed_n>2**31-1 or reversed_n< -2**31):
        return 0

    return reversed_n

print(reverse_int(-2**35))