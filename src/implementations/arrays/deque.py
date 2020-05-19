class Deque:
    """Implements https://en.wikipedia.org/wiki/Deque
    using a dynamic array with a ring buffer
    """
    def __init__(self, start_size=10):
        self.arr = [None for i in range(start_size)]
        self.end = 0    # could be any number in range [0, start_size)
        self.start = self.end
        self.load = 0

    def __str__(self):
        return str(self.arr)

    def enqueue(self, el):
        self.arr[self.end] = el
        self.end = (self.end + 1) % len(self.arr)  # modulo to wrap around
        self.load += 1
        print(f'Inserted {el} at index'
              f'{(self.end - 1 + len(self.arr)) % len(self.arr)}')
        self.check_resize()

    def dequeue(self):
        if self.start == self.end:
            print('Deque is empty, nothing to dequeue')
            return
        el = self.arr[self.start]
        self.arr[self.start] = None
        self.start = (self.start + 1) % len(self.arr)
        self.load -= 1
        print(f'Deuqueued {el}')
        self.check_resize()

    def push(self, el):
        self.enqueue(el)

    def pop(self):
        if self.start == self.end:
            print('Deque is empty, nothing to pop')
            return
        self.end = (self.end + len(self.arr) - 1) % len(self.arr)
        el = self.arr[self.end]
        self.arr[self.end] = None
        self.load -= 1
        print(f'Popped {el}')
        self.check_resize()

    def check_resize(self):
        if self.load <= 0.25 * len(self.arr):
            self.downsize()
        if self.load == len(self.arr):
            self.upsize()

    def upsize(self):
        self.resize(2)

    def downsize(self):
        self.resize(0.5)

    def resize(self, factor):
        new_arr = [None for i in range(int(len(self.arr) * factor))]
        new_i = 0
        i = self.start
        for _ in range(self.load):
            new_arr[new_i] = self.arr[i]
            new_i += 1
            i = (i + 1) % len(self.arr)
        self.arr = new_arr
        self.start = 0
        self.end = self.load
        print(f'Resized Deque with factor {factor}'
              f'to new size {len(self.arr)}')


if __name__ == '__main__':
    D = Deque(5)
    print(D)
    D.enqueue(1)
    print(D)
    D.enqueue(2)
    print(D)
    D.enqueue(3)
    print(D)
    D.enqueue(4)
    print(D)
    D.enqueue(5)
    print(D)
    D.enqueue(6)
    print(D)
    D.enqueue(7)
    print(D)
    D.dequeue()
    print(D)
    D.dequeue()
    print(D)
    D.pop()
    print(D)
    D.pop()
    print(D)
    D.dequeue()
    print(D)
    D.dequeue()
    print(D)
    D.dequeue()
    print(D)
    D.dequeue()
    print(D)
    D.push(1)
    print(D)
    D.push(2)
    print(D)
    D.push(3)
    print(D)
    D.push(4)
    print(D)
    D.pop()
    print(D)
    D.pop()
    print(D)
    D.pop()
    print(D)
    D.pop()
    print(D)

# [None, None, None, None, None]
# Inserted 1 at index 0
# Resized Deque with factor 0.5 to new size 2
# [1, None]
# Inserted 2 at index 1
# Resized Deque with factor 2 to new size 4
# [1, 2, None, None]
# Inserted 3 at index 2
# [1, 2, 3, None]
# Inserted 4 at index 3
# Resized Deque with factor 2 to new size 8
# [1, 2, 3, 4, None, None, None, None]
# Inserted 5 at index 4
# [1, 2, 3, 4, 5, None, None, None]
# Inserted 6 at index 5
# [1, 2, 3, 4, 5, 6, None, None]
# Inserted 7 at index 6
# [1, 2, 3, 4, 5, 6, 7, None]
# Deuqueued 1
# [None, 2, 3, 4, 5, 6, 7, None]
# Deuqueued 2
# [None, None, 3, 4, 5, 6, 7, None]
# Popped 7
# [None, None, 3, 4, 5, 6, None, None]
# Popped 6
# [None, None, 3, 4, 5, None, None, None]
# Deuqueued 3
# Resized Deque with factor 0.5 to new size 4
# [4, 5, None, None]
# Deuqueued 4
# Resized Deque with factor 0.5 to new size 2
# [5, None]
# Deuqueued 5
# Resized Deque with factor 0.5 to new size 1
# [None]
# Deque is empty, nothing to dequeue
# [None]
# Inserted 1 at index 0
# Resized Deque with factor 2 to new size 2
# [1, None]
# Inserted 2 at index 1
# Resized Deque with factor 2 to new size 4
# [1, 2, None, None]
# Inserted 3 at index 2
# [1, 2, 3, None]
# Inserted 4 at index 3
# Resized Deque with factor 2 to new size 8
# [1, 2, 3, 4, None, None, None, None]
# Popped 4
# [1, 2, 3, None, None, None, None, None]
# Popped 3
# Resized Deque with factor 0.5 to new size 4
# [1, 2, None, None]
# Popped 2
# Resized Deque with factor 0.5 to new size 2
# [1, None]
# Popped 1
# Resized Deque with factor 0.5 to new size 1
# [None]
