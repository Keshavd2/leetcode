def merge_interval(intervals):
    if intervals == []:
        return intervals
    
    intervals.sort()
    result = [intervals[0]]
    
    for i in range(1, len(intervals)):
        if intervals[i][0] >= result[-1][0] and intervals[i][0] <= result[-1][1]:
            result[-1] = [result[-1][0], max(result[-1][1], intervals[i][1])] 
        else:
            result.append(intervals[i])
    
    return result




a = [[1,3],[2,6],[8,10],[15,18]]
print(merge_interval(a))

