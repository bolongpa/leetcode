class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.k = k
        self.head = 0
        self.tail = 0
        self.queue = [None] * (self.k + 1)

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        else:
            if self.head > 0:
                self.head += -1
                self.queue[self.head] = value
            else:  # self.head == 0
                self.head = self.k
                self.queue[self.head] = value
            return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        else:
            self.queue[self.tail] = value
            self.tail += 1
            if self.tail > self.k:
                self.tail = 0
            return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        else:
            self.queue[self.head] = None
            self.head += 1
            if self.head > self.k:
                self.head = 0
            return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        else:
            self.tail += -1
            if self.tail < 0:
                self.tail = self.k
            self.queue[self.tail] = None
            return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.head]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return -1
        else:
            tail_id = self.tail - 1
            if tail_id >= 0:
                return self.queue[tail_id]
            else:  # tail_id == -1
                tail_id = self.k
                return self.queue[tail_id]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.head == self.tail

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        len = self.tail - self.head
        return len == -1 or len == self.k

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()