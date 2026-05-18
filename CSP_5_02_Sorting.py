import random


def bubbleSort(items):
    swaps = 0
    comparisons = 0
    n = len(items)

    for i in range(n):
        swapped = False
        for j in range(n - 1):
            comparisons += 1
            if items[j] > items[j + 1]:
                swaps += 1
                swapped = True
                items[j], items[j + 1] = items[j + 1], items[j]
        if not swapped:
            break

    return items, swaps, comparisons

def insertionSort(items):
    swaps = 0
    comparisons = 0

    for i in range(1, len(items)):
        current = items[i]
        j = i - 1

        while j >= 0:
            comparisons += 1

            if items[j] > current:
                swaps += 1
                items[j + 1] = items[j]
                j -= 1
            else:
                break

        items[j + 1] = current

    return items, swaps, comparisons


def selectionSort(items):
    swaps = 0
    comparisons = 0

    for i in range(len(items) - 1):
        minIndex = i

        for j in range(i + 1, len(items)):
            comparisons += 1

            if items[j] < items[minIndex]:
                minIndex = j

        swaps += 1
        items[i], items[minIndex] = items[minIndex], items[i]

    return items, swaps, comparisons


y = [9,8,7,6,5,4,3,2,1]

print(bubbleSort(y.copy()))
print(insertionSort(y.copy()))
print(selectionSort(y.copy()))

print()

x = [x for x in range(50)]
random.shuffle(x)

print(bubbleSort(x.copy()))
print(insertionSort(x.copy()))
print(selectionSort(x.copy()))
