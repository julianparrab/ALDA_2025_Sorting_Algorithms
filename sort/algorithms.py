import math


### split_and_sorted_approach ###
# Complejidad total:
# Mejor caso: O(n log n)
# Peor caso: O(n log n)
# Caso promedio: O(n log n)
def split_and_sorted_approach(arr):
    if len(arr) == 0:  # O(1)
        return []  # O(1)
    odds = filter(lambda number: number % 2 == 1, arr)  # O(n)
    even = filter(lambda number: number % 2 == 0, arr)  # O(n)

    odds = sorted(odds, key=lambda x: -x)  # O(n log n)
    even = sorted(even)  # O(n log n)

    return even + odds  # O(n)


### no_split_and_sorted_approach ###
# Complejidad total:
# Mejor caso: O(n log n)
# Peor caso: O(n log n)
# Caso promedio: O(n log n)
def no_split_and_sorted_approach(arr):
    if len(arr) == 0:  # O(1)
        return []  # O(1)
    return sorted(arr, key=lambda x: -x if x % 2 == 1 else x)  # O(n log n)


### full_sort_and_iterate_approach ###
# Complejidad total:
# Mejor caso: O(n log n)
# Peor caso: O(n log n)
# Caso promedio: O(n log n)
def full_sort_and_iterate_approach(arr):
    if len(arr) == 0:  # O(1)
        return []  # O(1)
    answer = []  # O(1)

    sorted_array = sorted(arr)  # O(n log n)
    for x in sorted_array:  # O(n)
        if x % 2 == 0:  # O(1)
            answer.append(x)  # O(1)

    reversed_sorted = sorted(arr, reverse=True)  # O(n log n)
    for x in reversed_sorted:  # O(n)
        answer.append(x)  # O(1)

    return answer  # O(1)


# There is another way to experimentally estimate the complexity of an algorithm
# This is by counting the elemental operations that the algorithm performs
# This could be a more precise way to estimate the complexity of an algorithm
# Take this function as an example for this approach
def split_and_sorted_approach_counting_elemental_operations(arr):
    elemental_operations = 0  # O(1)
    elemental_operations += 2  # O(1)
    n = len(arr)  # O(1)
    if len(arr) == 0:  # O(1)
        return []  # O(1)

    elemental_operations += 2 * n  # O(1)
    odds = filter(lambda number: number % 2 == 1, arr)  # O(n)
    even = filter(lambda number: number % 2 == 0, arr)  # O(n)

    elemental_operations += 2 * n * math.log(n, 2)  # O(n log n)
    odds = sorted(odds, key=lambda x: -x)  # O(n log n)
    even = sorted(even)  # O(n log n)
    elemental_operations += 2 * n  # O(1)

    return even + odds, elemental_operations  # O(1)


### Bubble Sort ###
# Complejidad total:
# Mejor caso (lista ordenada): O(n)
# Peor caso (lista en orden inverso): O(n^2)
# Caso promedio: O(n^2)
def bubble_sort(arr):
    n = len(arr)  # O(1)

    for i in range(n):  # O(n)
        swapped = False  # O(1)

        for j in range(0, n - i - 1):  # O(n - i)
            if arr[j] > arr[j + 1]:  # O(1)
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # O(1)
                swapped = True

        if not swapped:  # O(1)
            break  # O(1)

    return arr  # O(1)


### Selection Sort ###
# Complejidad total:
# Mejor caso: O(n^2)
# Peor caso: O(n^2)
# Caso promedio: O(n^2)
def selection_sort(arr):
    n = len(arr)  # O(1)

    for i in range(n):  # O(n)
        min_index = i  # O(1)
        for j in range(i + 1, n):  # O(n)
            if arr[j] < arr[min_index]:  # O(1)
                min_index = j  # O(1)

        arr[i], arr[min_index] = arr[min_index], arr[i]  # O(1)

    return arr


#### insertion_sort  ####
# Complejidad total:
# Mejor caso (lista ordenada): O(n)
# Peor caso (lista en orden inverso): O(n^2)
# Caso promedio: O(n^2)


def insertion_sort(arr):
    n = len(arr)  # O(1)

    for i in range(1, n):  # O(n)
        key = arr[i]  # O(1)
        j = i - 1  # O(1)

        while j >= 0 and arr[j] > key:  # O(n) en el peor caso
            arr[j + 1] = arr[j]  # O(1)
            j -= 1  # O(1)

        arr[j + 1] = key  # O(1)

    return arr  # O(1)


#### quicksort  ####
# Complejidad total:
# - Mejor caso: O(n log n)
# - Caso promedio: O(n log n)
# - Peor caso: O(n^2)


def quicksort(arr):
    if len(arr) <= 1:  # O(1)
        return arr  # O(1)

    pivot = arr[len(arr) // 2]  # O(1)
    left = [x for x in arr if x < pivot]  # O(n)
    middle = [x for x in arr if x == pivot]  # O(n)
    right = [x for x in arr if x > pivot]  # O(n)

    return quicksort(left) + middle + quicksort(right)  # O(n log n)
