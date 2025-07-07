def diff_of_lists(raw_lis1,lis2):
    if raw_lis1 is None or lis2 is None:
        raise ValueError("Input lists cannot be None")
    
    temp_combined = list(raw_lis1) + list(lis2)
    if not all(isinstance(i, int) for i in temp_combined):
        raise TypeError("Only integers are allowed in the lists")
    
    if not isinstance(raw_lis1, list):
        raw_lis1 = list(raw_lis1)

    if not isinstance(lis2, list):
        lis2 = list(lis2)
    
    lis1 = list(set(raw_lis1))
    result = []

    result = [i for i in lis1 if i not in lis2]

    return result

if __name__ == "__main__":
    raw_lis1 = [1, 2, 3]
    lis2 = [2, 4, 4]
    print(diff_of_lists(raw_lis1, lis2))
