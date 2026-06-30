# names=['Maria','Ayesha','Natalia']
# for index in range(len(names)):
#     print(index)

class CustomIterator:
    def __init__(self, limit):
        self.limit= limit

    def __iter__(self):
        self.number_of_students= 0
        return self
    
    def __next__(self):
        if self.number_of_students>= self.limit:
            raise StopIteration
        
        else:
            self.number_of_students+=1
            return self.number_of_students
        
it= CustomIterator(5)

for x in it:
    print(x)