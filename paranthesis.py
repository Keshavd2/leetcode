def min_swaps(s):
    # Your solution here
    open_paran = 0
    unmatch = 0

    for paran in s:
        if paran == "(":
            open_paran += 1
        else:
            if open_paran > 0:
                open_paran -= 1
            else:
                unmatch += 1
    return unmatch
    

print(min_swaps(")("))    # Expected: 1
print(min_swaps("))(("))  # Expected: 2
print(min_swaps("()"))    # Expected: 0
print(min_swaps("(())"))  # Expected: 0
print(min_swaps(")()("))  # Expected: 1