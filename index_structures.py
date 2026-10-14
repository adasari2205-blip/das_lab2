from linked_list import LineNumberList


class DictIndex:
    """Word -> linked list of line numbers, using Python's dictionary."""
    def __init__(self):
        self.data = {}

    def add(self, word, line_number):
        if word not in self.data:
            self.data[word] = LineNumberList()
        self.data[word].append(line_number)

    def search(self, word):
        return self.data.get(word)

    def iter_sorted(self):
        for word in sorted(self.data):
            yield word, self.data[word]

    def __len__(self):
        return len(self.data)


class TrieNode:
    __slots__ = ("children", "line_numbers")

    def __init__(self):
        self.children = {}
        self.line_numbers = None


class TrieIndex:
    """Trie keyed by characters; terminal nodes hold line-number lists."""
    def __init__(self):
        self.root = TrieNode()
        self.word_count = 0

    def add(self, word, line_number):
        node = self.root
        for character in word:
            child = node.children.get(character)
            if child is None:
                child = TrieNode()
                node.children[character] = child
            node = child
        if node.line_numbers is None:
            node.line_numbers = LineNumberList()
            self.word_count += 1
        node.line_numbers.append(line_number)

    def search(self, word):
        node = self.root
        for character in word:
            node = node.children.get(character)
            if node is None:
                return None
        return node.line_numbers

    def iter_sorted(self):
        # Iterative traversal avoids Python recursion limits for long words.
        stack = [(self.root, "", False)]
        while stack:
            node, prefix, visited = stack.pop()
            if visited:
                continue
            if node.line_numbers is not None:
                yield prefix, node.line_numbers
            for character in sorted(node.children, reverse=True):
                stack.append((node.children[character], prefix + character, False))

    def __len__(self):
        return self.word_count


class BSTNode:
    __slots__ = ("word", "line_numbers", "left", "right")

    def __init__(self, word, line_number):
        self.word = word
        self.line_numbers = LineNumberList()
        self.line_numbers.append(line_number)
        self.left = None
        self.right = None


class BSTIndex:
    """Unbalanced binary search tree keyed by complete words."""
    def __init__(self):
        self.root = None
        self.word_count = 0

    def add(self, word, line_number):
        if self.root is None:
            self.root = BSTNode(word, line_number)
            self.word_count = 1
            return

        node = self.root
        while True:
            if word == node.word:
                node.line_numbers.append(line_number)
                return
            if word < node.word:
                if node.left is None:
                    node.left = BSTNode(word, line_number)
                    self.word_count += 1
                    return
                node = node.left
            else:
                if node.right is None:
                    node.right = BSTNode(word, line_number)
                    self.word_count += 1
                    return
                node = node.right

    def search(self, word):
        node = self.root
        while node is not None:
            if word == node.word:
                return node.line_numbers
            node = node.left if word < node.word else node.right
        return None

    def iter_sorted(self):
        stack = []
        node = self.root
        while stack or node is not None:
            while node is not None:
                stack.append(node)
                node = node.left
            node = stack.pop()
            yield node.word, node.line_numbers
            node = node.right

    def __len__(self):
        return self.word_count


def build_index(index, input_filename):
    """Populate an index from a file and return it."""
    from text_utils import read_word_occurrences
    for word, line_number in read_word_occurrences(input_filename):
        index.add(word, line_number)
    return index


def write_index(index, output_filename):
    """Write words in ASCII lexicographic order and all line occurrences."""
    with open(output_filename, "w", encoding="ascii", newline="\n") as output:
        for word, line_numbers in index.iter_sorted():
            output.write(f"{word} : {line_numbers.as_text()}\n")
