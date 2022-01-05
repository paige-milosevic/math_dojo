
class MathDojo:
    def __init__(self):
        self.result = 0
    
    def add(self, num1, *nums):
        totalSum = num1
        for num in nums:
            totalSum += num
        self.result = self.result + totalSum
        return self
        # your code here
    
    def subtract(self, num1, *nums):
        totalSum = num1
        for num in nums:
            totalSum += num
        if self.result >= totalSum:
            self.result = self.result - totalSum
        else:
            self.result = totalSum - self.result

        return self
        # your code heres
# create an instance:s
md = MathDojo()
# to test:
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)	# should print 5
# run each of the methods a few more times and check the result!

