# Index Generation — DSA Lab Project

## Files
- `linked_list.py`: linked list storing every line-number occurrence.
- `text_utils.py`: reads words line by line using the specified separators.
- `index_structures.py`: Trie, ordinary BST, and Python dictionary implementations.
- `main.py`: required two-argument command-line utility.
- `benchmark.py`: generates six datasets and measures construction, 100,000 searches, and printing.
- `generate_graphs.py`: plots the three benchmark comparisons with Matplotlib.

## Requirements
Python 3.10+ recommended. Install Matplotlib for graphs:
```bash
python -m pip install matplotlib
```

## Generate an index
The default implementation is the dictionary:
```bash
python main.py input.txt output.txt
```
To select another implementation, change `IMPLEMENTATION` near the top of `main.py` to `"trie"` or `"bst"`. The command still takes exactly two filename arguments.

The parser preserves case and all non-separator characters. Words are separated by spaces/tabs, line breaks, `.`, `,`, `:`, and `;`. Line numbers are 1-based. Repeated occurrences are preserved, including repeated appearances on the same line.

## Benchmark and graphs
```bash
python benchmark.py
python generate_graphs.py
```
The benchmark creates datasets in `datasets/`, writes `benchmark_results.csv`, and the graph script saves three PNGs in `graphs/`.

The datasets contain at least 1,000,100 word occurrences and the specified distinct-word counts. They are synthetic, reproducible test data. The BST is deliberately an ordinary unbalanced BST, so the largest experiment may be slow. Run the benchmark when the computer can remain busy for a while.

## Notes
- Python string ordering is ASCII ordering for the printable-ASCII input guaranteed by the assignment.
- Construction timing includes linked-list creation and input scanning.
- Search timing measures 100,000 queries drawn from the dataset vocabulary.
- Printing timing includes sorting/traversal and writing the complete index file.
