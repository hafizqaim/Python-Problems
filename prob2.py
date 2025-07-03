def recursive_sum(n):
    if n <= 0:
        return 0
    elif n < 10:
        return n
    else:
        sum = (n % 10) + recursive_sum(n // 10)
        return recursive_sum(sum)

num = int(input("Enter a number to check digits sum: "))  
print(recursive_sum(num))