intervals1 = [[1,3],[6,9]]
newInterval1 = [2,5]
intervals2 = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval2 = [4,9]


def insert(intervals, newInterval):
    result = []
    """
    for interval in intervals:

        # CASE 1
        if interval[1] < newInterval[0]:
            result.append(interval)

        # CASE 2
        elif interval[0] > newInterval[1]:
            result.append(newInterval)
            newInterval = interval

        # CASE 3
        else:
            newInterval = [
                min(interval[0], newInterval[0]),
                max(interval[1], newInterval[1])
            ]

    result.append(newInterval)

    return result
    """

print(insert(intervals1, newInterval1))
print(insert(intervals2, newInterval2))