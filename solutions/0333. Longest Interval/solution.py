class Solution:
    def solve(self, intervals):
        result = []
        intervals.sort(key=lambda interval: interval[0])

        start, end = intervals[0]
        for interval in intervals:
            # can't be merged, append the length directly and reassign the bounds
            if interval[0] > end:
                result.append(end - start + 1)
                start, end = interval
            # can be merged, compare the upper bound before merging
            else:
                end = max(end, interval[1])
        result.append(end - start + 1)

        return max(result)
