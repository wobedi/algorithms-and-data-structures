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
              f' {(self.end - 1 + len(self.arr)) % len(self.arr)}')
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
              f' to new size {len(self.arr)}')


if __name__ == '__main__':
    D = Deque(5)
    print(D)

    for i in range(8):
        D.enqueue(i)
        print(D)

    # Basically simulating a step-debug here for illustration purposes
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
