class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        # adds the input value into the heap; this method should ensure that the inserted value is in the correct spot in the heap
        # add value to storage then use bubble up
        self.storage.append(value)
        self._bubble_up(self.get_size()-1)

    def delete(self):
        pass
        # removes and returns the 'topmost' value from the heap; this method needs to ensure that the heap property is maintained after the topmost element has been removed.

    def get_max(self):
        # returns the maximum value in the heap _in constant time_.
        # This will be the root
        return self.storage[0]

    def get_size(self):
        # returns the number of elements stored in the heap. AKA just find length
        return len(self.storage)

    def _bubble_up(self, index):
        # moves the element at the specified index "up" the heap by swapping it with its parent if the parent's value is less than the value at the specified index.
        # keep bubbling up until we've either reached the top of heap or we've reached a point where parent is the higher priority
        while index > 0:
            # on a singelbubble up iteration:
            # get the parent index
            parent = (index - 1) // 2
            # compare the child against the value of the parent
            # if the child's value is higher priority than parent's value
            if self.storage[index] > self.storage[parent]:
                # swap em
                self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
                # update the child's index to be the new index
                index = parent
            # otherwise, child is at a valid spot
            else:
              # stop bubbling bruh
                break

    def _sift_down(self, index):
        pass
        # grabs the indices of this element's children and determines which child has a larger value. If the larger child's value is larger than the parent's value, the child element is swapped with the parent.
