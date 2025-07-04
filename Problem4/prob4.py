def missing_character(alphaList):
    if not alphaList or len(alphaList) < 2:
        raise ValueError("input list should contain 
        at least 2 items")
    
    if not all(isinstance(c, str) and len(c) == 1 for c in alphaList):
        return None
        
    if not all(c.isalpha() for c in alphaList):
        return None
        
    for i in range(len(alphaList) - 1):
        if ord(alphaList[i + 1]) - ord(alphaList[i]) != 1:
            print(f"Orignal Array is: {alphaList}")
            return chr(ord(alphaList[i]) + 1)
    return None


if __name__ == '__main__':
    alphaList = ['A', 'B', 'C', 'E', 'F']
    print(f"Missing character in the sequence is: {missing_character(alphaList)}")
