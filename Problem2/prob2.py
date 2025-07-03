def recursive_sum(n):
    if n <= 0:
        return 0
    elif n < 10:
        return n
    else:
        digitSum = (n % 10) + recursive_sum(n // 10)
        return recursive_sum(digitSum)

if __name__ == '__main__':
    num = int(input("Enter a number to check digits sum: "))  
    print(recursive_sum(num))
