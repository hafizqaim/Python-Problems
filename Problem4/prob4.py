def missing_character(alphaList):
    alphaList.sort()
    for i in range(len(alphaList) - 1):
        if ord(alphaList[i + 1]) - ord(alphaList[i]) != 1:
            print(f"Orignal Array is: {alphaList}")
            return chr(ord(alphaList[i]) + 1)
    return None

try:
    alphaList = []
    input_count = 0
    gap_found = False 

    while input_count < 26:
        while True:
            inputChar = input(f"Enter character {input_count + 1} (or -1 to stop): ")

            if inputChar == "-1":
                if len(alphaList) >= 2:
                    break  
                else:
                    print("At least 2 characters are required to find a missing character.")
                    continue

            if len(inputChar) != 1 or not inputChar.isalpha():
                print("Please enter a single alphabet character.")
                continue

            if len(alphaList) > 0:
                if alphaList[-1].isupper() and not inputChar.isupper():
                    print("Input character must be Upper case to match previous characters.")
                    continue

                if alphaList[-1].islower() and not inputChar.islower():
                    print("Input character must be Lower case to match previous characters.")
                    continue

                gap = ord(inputChar) - ord(alphaList[-1])

                if not gap_found:
                    if gap > 2 or gap <= 0:
                        print("Input character must be next in sequence with a gap of at most 2.")
                        continue

                    if gap == 2:
                        gap_found = True

                else:
                    while True:
                        gap = ord(inputChar) - ord(alphaList[-1])
                        if gap == 1:
                            break
                        else:
                            print("Input character must be the next letter in the sequence now.")
                            inputChar = input(f"Enter character {input_count + 1}: ")

            alphaList.append(inputChar)
            input_count += 1
            break  

        if inputChar == "-1":
            break

except ValueError as e:
    print(f"Error: {e}")

if len(alphaList) >= 2:
    print(f"Missing character in the sequence is: {missing_character(alphaList)}")
else:
    print("Not enough characters to find the missing one.")