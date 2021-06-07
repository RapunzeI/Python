class Queue:
    def __init__(self, q = None):
        if q == None:
            self.q = []
        else:
            self.q = q
    
    def isEmpty(self):
        return (len(self.q) == 0)

    def enqueue(self, item):
        return self.q.append(item)

    def dequeue(self):
        # if len(self) == 0:
        #     raise KeyboardInterrupt('dequeue from empty queue')
        # return self.q.pop(0)
        try:
            return self.q.pop(0)
        except:
            pass

    def __eq__(self, other):
        return self.q == other.q
    
    def __len__(self):
        return len(self.q)

    def __repr__(self):
        return 'Queue({})'.format(self.q)