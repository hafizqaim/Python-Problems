def diff_of_lists(lis1,lis2):
    if lis1 is None or lis2 is None:
        raise ValueError("Input lists cannot be None")
    
    temp_combined = list(lis1) + list(lis2)
    if not all(isinstance(i, int) for i in temp_combined):
        raise TypeError("Only integers are allowed in the lists")
    
    if not isinstance(lis1, list):
        lis1 = list(lis1)

    if not isinstance(lis2, list):
        lis2 = list(lis2)
    
    result = []

    result = [i for i in lis1 if i not in lis2]

    return result

if __name__ == "__main__":
    lis1 = [1, 2, 2]
    lis2 = []
    print(diff_of_lists(lis1, lis2))
