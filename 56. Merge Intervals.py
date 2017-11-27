# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        out=list()
        for i in sorted(intervals,key=lambda i:i.start):
            if out and i.start<=out[-1].end:
                out[-1].end= max(i.end,out[-1].end)
            else:
                out.append(i);
        return out


        
