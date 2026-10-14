from pathlib import Path
from index_structures import DictIndex, TrieIndex, BSTIndex, build_index, write_index

root = Path(__file__).resolve().parent
source = root / "test_input.txt"
expected_words = ["Data", "and", "are", "data", "helps", "is", "problems", "solve", "structures", "useful"]

for cls in (DictIndex, TrieIndex, BSTIndex):
    index = build_index(cls(), str(source))
    assert len(index) == 10, (cls.__name__, len(index))
    assert list(word for word, _ in index.iter_sorted()) == expected_words
    assert list(index.search("Data")) == [1, 2]
    assert list(index.search("useful")) == [1, 2]
    assert index.search("missing") is None
    out = root / f"test_output_{cls.__name__}.txt"
    write_index(index, str(out))
    out.unlink()
print("All small correctness tests passed for Trie, BST, and Dictionary.")
