import random
import time
import os

from src.lab04.io_txt_csv import write_csv
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort, counting_sort, merge_sort
from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast


def benchmark(results, task, n, name, function, numbers, extra=(), runs=1, repeats=5):
    if function is None:
        results.append((task, n, name, "> 60.0"))
        return

    best = float("inf")

    for i in range(repeats):
        start = time.perf_counter()

        for j in range(runs):
            function(numbers.copy(), *extra)

        finish = time.perf_counter()
        seconds = (finish - start) / runs

        if seconds < best:
            best = seconds

    results.append((task, n, name, best))


def search_all(numbers, queries, function):
    for x in queries:
        function(numbers, x)


def main():
    random.seed(42)
    results = []

    print("Сравнение пяти алгоритмов сортировки на разных размерах списков...")

    algorithms = [
        ("sorted", sorted),
        ("merge_sort", merge_sort),
        ("bubble_sort", bubble_sort),
        ("insertion_sort", insertion_sort),
        ("selection_sort", selection_sort)
    ]

    for n in (1000, 10000, 100000):
        numbers = []

        for i in range(n):
            numbers.append(random.randint(-10000, 10000))

        for name, function in algorithms:
            runs = 1
            repeats = 5

            if name == "sorted":
                runs = 100

            if n == 100000:
                repeats = 1

            if n == 100000 and name in ("bubble_sort", "insertion_sort", "selection_sort"):
                function = None

            benchmark(results, "sort", n, name, function, numbers, runs=runs, repeats=repeats)

    print("Сравнение встроенной сортировки Python и сортировки подсчётом...")

    n = 1000000
    numbers = []

    for i in range(n):
        numbers.append(random.randint(0, 100))

    benchmark(results, "count", n, "sorted", sorted, numbers, runs=5, repeats=3)
    benchmark(results, "count", n, "counting_sort", counting_sort, numbers, (0, 100), 5, 3)

    print("Сравнение линейного и бинарного поиска...")

    n = 100000
    numbers = []
    queries = []

    for i in range(n):
        numbers.append(random.randint(-100000, 100000))

    for i in range(10000):
        queries.append(random.randint(-100000, 100000))

    benchmark(results, "search", n, "linear", search_all, numbers, (queries, linear_search), 1, 1)
    benchmark(results, "search", n, "sort_only", sorted, numbers, runs=1, repeats=1)

    ordered = sorted(numbers)

    benchmark(results, "search", n, "binary", search_all, ordered, (queries, binary_search), 10, 1)

    print("Сравнение полного перебора и быстрого алгоритма Two Sum...")

    for n in (1000, 10000):
        numbers = random.sample(range(-100000, 100000), n)

        indexes = random.sample(range(n), 2)
        target = numbers[indexes[0]] + numbers[indexes[1]]

        benchmark(results, "sum", n, "two_sum_brute", two_sum_brute, numbers, (target,), 1, 1)
        benchmark(results, "sum", n, "two_sum_fast", two_sum_fast, numbers, (target,), 100, 1)

    print(f"\n{'task':<10} | {'n':<10} | {'impl':<15} | seconds")
    print("-" * 55)

    for task, n, name, seconds in results:
        if isinstance(seconds, str):
            value = seconds
        else:
            value = f"{seconds:.6f}"

        print(f"{task:<10} | {n:<10} | {name:<15} | {value}")

    os.makedirs("data/lab07", exist_ok=True)

    write_csv(
        results,
        "data/lab07/bench.csv",
        header=("task", "n", "impl", "seconds")
    )

    print("\nРезультаты сохранены в data/lab07/bench.csv")


if __name__ == "__main__":
    main()
