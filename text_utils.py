import re

# A word ends at spaces/tabs, line breaks, or any of . , : ;
_SPLIT_RE = re.compile(r"[ \t\r\n.,;:]+")


def split_words(line):
    """Split one input line without changing case or other word characters."""
    return (part for part in _SPLIT_RE.split(line) if part)


def read_word_occurrences(filename):
    """Yield (word, 1-based line number), streaming the file line by line."""
    with open(filename, "r", encoding="ascii", errors="strict", newline=None) as file:
        for line_number, line in enumerate(file, start=1):
            for word in split_words(line):
                yield word, line_number
