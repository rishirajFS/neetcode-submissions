import heapq
class MedianFinder:

    def __init__(self):
        self.small=[]
        self.big=[]

    def addNum(self, num: int) -> None:
        if not(self.small):
            heapq.heappush(self.small, -num)
        elif num<= -self.small[0]:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.big, num)
        if len(self.small) > len(self.big) + 1:
            value = heapq.heappop(self.small)
            heapq.heappush(self.big, -value)

        elif len(self.big) > len(self.small) + 1:
            value = heapq.heappop(self.big)
            heapq.heappush(self.small, -value)

    def findMedian(self) -> float:
        if((len(self.small)+len(self.big))%2==0):
            return (-self.small[0]+self.big[0])/2
        else:
            if len(self.small) > len(self.big):
                return -self.small[0]
            else:
                return self.big[0]
        