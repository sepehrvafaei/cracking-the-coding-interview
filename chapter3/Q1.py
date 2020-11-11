#solution 1: each stack has fixed length
class MultiStack:
    def __init__(self,capacity):
        self.capacity=capacity
        self.numOfStacks=3
        self.sizes=[0 for i in range(self.numOfStacks)]
        self.values=[0 for i in range(self.capacity*self.numOfStacks)]

    def isEmpty(self,stackNum):
        return self.sizes[stackNum]==0

    def isFull(self,stackNum):
        return self.sizes[stackNum]==self.capacity

    def push(self,stackNum,data):
        if self.isFull(stackNum):print('FullError')
        else:
            self.sizes[stackNum]+=1
            index=self.capacity*stackNum+self.sizes[stackNum]-1
            self.values[index]=data

    def pop(self,stackNum):
        if self.isEmpty(stackNum):print('EmptyError')
        else:
            index=self.capacity*stackNum+self.sizes[stackNum]-1
            self.values[index]=0
            self.sizes[stackNum]-=1

    def top(self,stackNum):
        if self.isEmpty(stackNum):print('EmptyError')
        else:
            index=self.capacity*3+self.sizes[stackNum]-1
            return self.values[index]
    
