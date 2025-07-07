def diff_of_lists(lis1,lis2):
    if lis1 is None or lis2 is None:
        raise ValueError("Input lists cannot be None")
    
    lis1 = list(lis1)
    lis2 = set(lis2)
    if (
        any(not isinstance(i, int) for i in lis1)
        or any(not isinstance(i, int) for i in lis2)
    ):
        raise TypeError("Only integers are allowed in list2")

    result = [i for i in lis1 if i not in lis2]

    return result

if __name__ == "__main__":
    lis1 = [1, 2, 2]
    lis2 = []
    print(diff_of_lists(lis1, lis2))
