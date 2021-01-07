class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.queue = [None] * (k + 1)
        self.head = 0
        self.tail = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.queue[self.tail] = value
            self.tail += 1
            if self.tail > self.k:
                self.tail = 0
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.queue[self.head] = None
            self.head += 1
            if self.head > self.k:
                self.head = 0
            return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            tail_id = self.tail - 1
            if tail_id >= 0:
                return self.queue[tail_id]
            else:
                return self.queue[self.k]

    def isEmpty(self) -> bool:
        return self.tail == self.head

    def isFull(self) -> bool:
        return self.tail == self.head - 1 or self.tail - self.head == self.k

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
