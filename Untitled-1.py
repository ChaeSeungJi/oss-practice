class Sample:
    counter2=0
    def __init__(self):
        self.counter=0
    def numEven(self,n):
        for k in range(n):
            if k%2==0:
                self.counter+=1
                Sample.counter2+=1
        return self.counter


s1 = Sample()
s2 = Sample()
s1.numEven(15)
s2.numEven(15)
print(s1.counter,s1.counter2,Sample.counter2) # ㅇㄹㄴㅇ