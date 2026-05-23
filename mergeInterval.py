def merge_interval(intervals):
    if intervals == []:
        return intervals
    
    intervals.sort()
    result = [intervals[0]]
    
    for i in range(1, len(intervals)):
        if intervals[i][0] >= result[-1][0] and intervals[i][0] <= result[-1][1]:
            if result[-1][1] > intervals[i][1]:
                new_interval = [result[-1][0], result[-1][1]]
            else:
                new_interval = [result[-1][0], intervals[i][1]]
            result.pop()
            result.append(new_interval)
        else:
            result.append(intervals[i])
    
    return result




a = [[1,4],[0,0]]
print(merge_interval(a))

