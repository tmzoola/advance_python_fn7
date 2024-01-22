class MyIterator:
    
    def __init__(self,data):
        self.data = data
        self.index = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index<len(self.data):
            result = self.data[self.index]
            self.index +=1
            return result
        else:
            raise StopIteration


my_list = [1,2,3,5,4]
data = MyIterator(my_list)

iter(my_list)

print(next(my_list))
print(next(data))
print(next(data))
print(next(data))
print(next(data))
