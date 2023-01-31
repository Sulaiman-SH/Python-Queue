class Queue:
    def __init__(self):
        self.queue = list()
    
    def add(self, value):
        if value not in self.queue:
            self.queue.insert(0, value)
            return True
        return False
        
    
    def size(self):
        return len(self.queue)
    
    def show(self):
        return self.queue

    def pop(self):
        return self.queue.pop(0)
    
    def addENd(self, value):
        self.queue.append(value)
    
    def deleteE(self):
        self.queue.pop()
    
    def deleteF(self):
        self.queue.pop(0)



Q = Queue()
Q.add("MON")
Q.add("TUE")
Q.add("WED")
Q.addENd("SAT")
print(Q.show())
Q.deleteE()
print(Q.show())
Q.deleteF()
print(Q.show())
print("Size of the queue", Q.size())
print(Q.show())
print(Q.pop())
print(Q.show())
print(Q.pop())
print(Q.show())