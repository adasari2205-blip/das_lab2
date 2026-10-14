import argparse
from index_structures import DictIndex, TrieIndex, BSTIndex, build_index, write_index

# Change this to "dict", "trie", or "bst" to choose the implementation.
# The command line still takes exactly the required two filenames.
IMPLEMENTATION = "dict"
IMPLEMENTATIONS = {
    "dict": DictIndex,
    "trie": TrieIndex,
    "bst": BSTIndex,
}


def main():
    parser = argparse.ArgumentParser(
        description="Generate a lexicographically ordered word/line index."
    )
    parser.add_argument("input_file", help="input text filename")
    parser.add_argument("output_file", help="output index filename")
    args = parser.parse_args()

    index = IMPLEMENTATIONS[IMPLEMENTATION]()
    build_index(index, args.input_file)
    write_index(index, args.output_file)
    print(f"Indexed {len(index)} distinct words into {args.output_file}")


if __name__ == "__main__":
    main()
