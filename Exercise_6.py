def add_0_to_10(n) :
    if n :
        sum = n + add_0_to_10(n-1)
    else :
        return 0
    return sum

print(add_0_to_10(10))