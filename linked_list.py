class LineNode:
    """One occurrence of a word, storing the line where it appeared."""
    __slots__ = ("line_number", "next")

    def __init__(self, line_number):
        self.line_number = line_number
        self.next = None


class LineNumberList:
    """Singly linked list that preserves every occurrence in input order."""
    __slots__ = ("head", "tail", "length")

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, line_number):
        node = LineNode(line_number)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length += 1

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.line_number
            current = current.next

    def __len__(self):
        return self.length

    def as_text(self):
        return ", ".join(str(number) for number in self)
