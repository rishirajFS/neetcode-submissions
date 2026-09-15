class MedianFinder:

    def __init__(self):
        self.arr=[]
        return None

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        return None

    def findMedian(self) -> float:
        self.arr.sort()
        if(len(self.arr)%2==0):
            median=(self.arr[len(self.arr)//2]+self.arr[len(self.arr)//2-1])/2
            return median
        else:
            median=(self.arr[(len(self.arr)-1)//2])
            return median
        