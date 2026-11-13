import argparse
from pathlib import Path
from src.lib.text import normalize, tokenize, count_freq, top_n


def main():
    """
    The function processes a text file using the `cat` and `stats` commands

    cat:
        --input: a parameter that causes the program to output the contents of a file
        -n: a parameter that outputs content with line numbering

    stats:
        --input: a parameter that causes the program to output the contents of a file
        --top: a parameter that specifies the number of words in the result
    """
    parser = argparse.ArgumentParser(description="Text file processing tools")
    commands = parser.add_subparsers(dest="command", required=True)

    cat_cmd = commands.add_parser("cat", help="Display file contents")
    cat_cmd.add_argument("--input", required=True, help="Input file")
    cat_cmd.add_argument("-n", action="store_true", help="Number lines starting from 1")

    stats_cmd = commands.add_parser("stats", help="Display the most frequent words")
    stats_cmd.add_argument("--input", required=True, help="Input file")
    stats_cmd.add_argument("--top", type=int, default=5, help="Number of words (default: 5)")

    args = parser.parse_args()
    file_path = Path(args.input)

    if args.command == "cat":
        if not file_path.is_file():
            raise FileNotFoundError(f"File is not found: {file_path}")

        with open(file_path, encoding="utf-8", newline="") as file:
            lines = file.readlines()

        if args.n:
            for i in range(len(lines)):
                print(f"{i+1:>4}\t{lines[i]}", end="")
        else:
            for i in range(len(lines)):
                print(lines[i], end="")

    elif args.command == "stats":
        if not file_path.is_file():
            raise FileNotFoundError(f"File is not found: {file_path}")
        if args.top < 0:
            raise ValueError("The number of words in the top list cannot be negative.")

        with open(file_path, encoding="utf-8", newline="") as file:
            content = file.read()

        cleaned = normalize(content)
        word_list = tokenize(cleaned)
        frequencies = count_freq(word_list)
        result = top_n(frequencies, args.top)

        width = len("слово")
        for word, count in result:
            width = max(width, len(word))

        title = f'{"слово":<{width}} | частота'
        print(title)
        print("-" * len(title))

        for word, count in result:
            print(f"{word:<{width}} | {count}")

        print("...")


if __name__ == "__main__":
    main()
