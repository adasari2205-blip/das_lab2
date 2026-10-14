import csv
from pathlib import Path
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
RESULTS_FILE = ROOT / "benchmark_results.csv"
GRAPH_DIR = ROOT / "graphs"


def main():
    if not RESULTS_FILE.exists():
        raise SystemExit("benchmark_results.csv not found. Run benchmark.py first.")

    with open(RESULTS_FILE, newline="", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    GRAPH_DIR.mkdir(exist_ok=True)
    measures = [
        ("construction_seconds", "Construction time (seconds)", "construction_time.png"),
        ("100000_searches_seconds", "Time for 100,000 searches (seconds)", "search_time.png"),
        ("printing_seconds", "Lexicographic printing time (seconds)", "printing_time.png"),
    ]
    implementations = ["Trie", "BST", "Dictionary"]

    for field, ylabel, filename in measures:
        plt.figure()
        for implementation in implementations:
            selected = sorted(
                (row for row in rows if row["implementation"] == implementation),
                key=lambda row: int(row["distinct_words"]),
            )
            x = [int(row["distinct_words"]) for row in selected]
            y = [float(row[field]) for row in selected]
            plt.plot(x, y, marker="o", label=implementation)
        plt.xlabel("Number of distinct words")
        plt.ylabel(ylabel)
        plt.title(ylabel + " by implementation")
        plt.xscale("log")
        plt.grid(True, which="both", linestyle=":")
        plt.legend()
        plt.tight_layout()
        plt.savefig(GRAPH_DIR / filename, dpi=160)
        plt.close()
        print(f"Saved {GRAPH_DIR / filename}")


if __name__ == "__main__":
    main()
