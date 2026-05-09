def daily_temperatures(temperatures):
    """Return wait days until warmer temperature for each day."""
    answer = [0] * len(temperatures)
    stack = []  # stores indices of days waiting for a warmer day

    for i, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            idx = stack.pop()
            answer[idx] = i - idx
        stack.append(i)

    return answer
        
    

print(daily_temperatures([73,74,75,71,69,72,76,73]))  # [1,1,4,2,1,1,0,0]
print(daily_temperatures([30,40,50,60]))               # [1,1,1,0]
print(daily_temperatures([30,60,90]))                  # [1,1,0]
print(daily_temperatures([90,80,70,60]))               # [0,0,0,0]