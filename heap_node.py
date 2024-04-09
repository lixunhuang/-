class heap:
    def __init__(self, val):
        self.heap = [val]

    def left(self, index):
        return self.heap[2 * index + 1] if 2 * index + 1 < len(self.heap) else None

    def right(self, index):
        return self.heap[2 * index + 2] if 2 * index + 2 < len(self.heap) else None


def inject(heap, node):
    heap.append(node)
    index = len(heap) - 1
    while index != 0 and heap[index] < heap[(index - 1) // 2]:
        heap[index], heap[(index - 1) // 2] = heap[(index - 1) // 2], heap[index]
        index = (index - 1) // 2


def iterate(heap):
    for i in range((len(heap.heap) - 1) // 2 + 1):
        print('\n {} \n {} \n {}'.format(heap.heap[i], heap.left(i), heap.right(i)))


heap1 = heap(2)
inject(heap1.heap, 3)
inject(heap1.heap, 4)
inject(heap1.heap, 1)
iterate(heap1)



