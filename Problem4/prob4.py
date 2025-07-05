def missing_character(alphaList):
    if not alphaList or len(alphaList) < 2:
        raise ValueError("Input list should contain at least 2 items")
    
    if not all(isinstance(c, str) and len(c) == 1 for c in alphaList):
        raise ValueError("All items in the list must be single characters.")
        
    if not all(c.isalpha() for c in alphaList):
        raise ValueError("All characters must be alphabetic.")
        
    for i in range(len(alphaList) - 1):
        if ord(alphaList[i + 1]) - ord(alphaList[i]) != 1:
            print(f"Orignal Array is: {alphaList}")
            return chr(ord(alphaList[i]) + 1)
    return "None. No missing character found in the sequence."


if __name__ == '__main__':
    alphaList = ['A', 'B', 'C', 'E', 'F']
    print(f"Missing character in the sequence is: {missing_character(alphaList)}")
