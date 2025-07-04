def create_phone_number(numbers):
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of integers.")
    
    if len(numbers) != 10:
        raise ValueError("List must contain exactly 10 integers.")
    
    for num in numbers:
        if not isinstance(num, int) or not (0 <= num <= 9):
            raise ValueError("All elements must be integers between 0 and 9.")

    return f"({numbers[0]}{numbers[1]}{numbers[2]}) {numbers[3]}{numbers[4]}{numbers[5]}-{numbers[6]}{numbers[7]}{numbers[8]}{numbers[9]}"

if __name__ == "__main__":
    numbers = [1,2,3,4,5,6,7,8,9,0]
    create_phone_number(numbers)
