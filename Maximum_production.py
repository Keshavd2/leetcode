def max_product(nums):
    max_number = float("-inf")
    max_product = float("-inf")
    current_product = 1
    negative_product = None

    for num in nums:
        if num > max_number:
            max_number = num
        
        current_product *= num

        if current_product < 0:
            if negative_product != None:
                current_product *= negative_product
                negative_product = None
            else:
                negative_product = current_product
                current_product = 1
                continue

        elif current_product == 0:
            negative_product = None
            current_product = 1
            continue
        
        if current_product > max_product:
            max_product = current_product

    return max(max_number, max_product)


    

print(max_product([2, 3, -2, 4]))   # Expected: 6
print(max_product([-2, 0, -1]))     # Expected: 0
print(max_product([-2, 3, -4]))     # Expected: 24
print(max_product([-2]))            # Expected: -2
print(max_product([-1, -2, -3, 4]))          # Expected: 2