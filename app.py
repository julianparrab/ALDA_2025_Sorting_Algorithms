import sys
from sort import algorithms
from sort import execution_time_gathering
import matplotlib.pyplot as plt

if __name__ == "__main__":
    minimum_size = 1000
    maximum_size = 4000
    step = 200
    samples_by_size = 10

    table = execution_time_gathering.take_execution_time(minimum_size, maximum_size, step, samples_by_size)

    print(
        "Size | Split and Sorted | No Split and Sorted | Full Sort and Iterate | Bubble_sort | Selection_sort | Insertion_sort | Quick_sort"
    )
    for row in table:
        print(row)

    # Get Data for Plot
    sizes = [row[0] for row in table]
    split_sorted_times = [row[1] for row in table]
    no_split_sorted_times = [row[2] for row in table]
    full_sort_iterate_times = [row[3] for row in table]
    bubble_sort_times = [row[4] for row in table]
    selection_sort_times = [row[5] for row in table]
    insertion_sort_times = [row[6] for row in table]
    quick_sort_times = [row[7] for row in table]

    # Execution Time Plot
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, split_sorted_times, label="Split and Sorted O(n log n)", marker="o")
    plt.plot(sizes, no_split_sorted_times, label="No Split and Sorted O(n log n)", marker="s")
    plt.plot(sizes, full_sort_iterate_times, label="Full Sort and Iterate O(n log n)", marker="^")
    plt.plot(sizes, bubble_sort_times, label="Bubble Sort O(n^2)", marker="d")
    plt.plot(sizes, selection_sort_times, label="Selection Sort O(n^2)", marker="x")
    plt.plot(sizes, insertion_sort_times, label="Insertion Sort O(n^2)", marker="*")
    plt.plot(sizes, quick_sort_times, label="Quick Sort O(n log n)", marker="v")

    plt.xlabel("Input Size")
    plt.ylabel("Execution Time (ms)")
    plt.title("Execution Time of Sorting Algorithms")
    plt.legend()
    plt.grid()
    plt.show()
