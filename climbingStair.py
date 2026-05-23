def climbing_stairs(n, remember = {}):
    if n == 2:
        return 2
    if n == 1:
        return 1
    
    if n in remember:
        return remember[n]
    
    remember[n] = climbing_stairs(n - 2, remember) + climbing_stairs(n - 1, remember)
    return remember[n]

a = 5
print(climbing_stairs(a))