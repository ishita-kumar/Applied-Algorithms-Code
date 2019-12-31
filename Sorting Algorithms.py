# Importing libraries
import random
import time
import copy
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(10**7)
# AIM: Implement Insertion Sort, MergeSort and Deterministic QuickSort.

# Define Random() function to compute Random Input array
def Random(size):
    A = []
    for i in range(0, size):
        A.append(random.randint(1, size))
    return A

def plot(sizes, insertionsort, mergeSort,quicksort): 
    plt.xlabel('Number of Elements in Array', fontsize=30)
    plt.ylabel('Time(In Seconds)', fontsize=30)
    plt.plot(sizes, insertionsort, label='Insertion Sort')
    plt.plot(sizes, mergeSort, label='MergeSort')
    plt.plot(sizes, quicksort, label='Quicksort')
    plt.legend()
    plt.show()

# Input plot for Large Random Values
def input_plot1():
    avg_insertion = []
    avg_merge = []
    avg_quicksort = []
    sum_insertion = 0
    sum_merge = 0
    sum_quicksort = 0
    # sizes = [5000, 10000, 15000, 20000, 25000, 30000]
    sizes = [500, 1000, 1500, 2000, 2500, 3000]
    # Iterating through the loop for given Sizes
    for i in sizes:
        Arr1, Arr2, Arr3 = [], [], []
        sum1 = 0
        sum2 = 0
        # Executing Array[Size] for 3 iterations
        for k in range(0, 3):
            Arr1 = Random(i)
            Arr2 = copy.deepcopy(Arr1)
            Arr3 = copy.deepcopy(Arr1)
            # time.time function used for Computing start and end time
            t0 = time.time()
            insertionsort(Arr1)
            t1 = time.time()
            insertion_time = t1 - t0
            sum_insertion = insertion_time + sum_insertion
            t2 = time.time()
            mergeSort(Arr2)
            t3 = time.time()
            merge_time = t3 - t2
            sum_merge = merge_time + sum_merge
            t4 = time.time()
            quickSort(Arr3, 0, len(Arr3) - 1)
            t5 = time.time()
            quicksort_time = t5 - t4
            sum_quicksort = quicksort_time + sum_quicksort

        # Computing the average time taken for Insertion Sort
        sum_insertion = sum_insertion / 3
        avg_insertion.append(sum_insertion)

        # Computing the average time taken for Selection Sort
        sum_merge = sum_merge / 3
        avg_merge.append(sum_merge)

        # Computing the average time taken for Selection Sort
        sum_quicksort = sum_quicksort / 3
        avg_quicksort.append(sum_quicksort)

    plt.title('Sort Performance for Large Random Inputs', fontsize=55,
              ha='center')
    plot(sizes,avg_insertion,avg_quicksort,avg_merge)

# Plot for Non decreasing Random Values of Input
def input_plot2():
    Array_insertion = []
    Array_merge = []
    Array_quicksort = []
    Arr1, Arr2, Arr3 = [], [], []
    # sizes = [500, 1000, 1500, 2000, 2500, 3000]
    sizes = [5000, 10000, 15000, 20000, 25000, 30000]
    # Iterating through the loop for given Sizes
    for i in sizes:
        Arr1 = Random(i)
        Arr1.sort()
        Arr2 = copy.deepcopy(Arr1)
        Arr3 = copy.deepcopy(Arr1)
        # time.time function used for Computing start and end time
        t0 = time.time()
        insertionsort(Arr1)
        t1 = time.time()
        insertion_time = t1 - t0
        t2 = time.time()
        mergeSort(Arr2)
        t3 = time.time()
        merge_time = t3 - t2
        t4 = time.time()
        quickSort(Arr3, 0, len(Arr3) - 1)
        t5 = time.time()
        quicksort_time = t5 - t4
        # Appending Insertion sort time into Array
        Array_insertion.append(insertion_time)
        # Appending Selection sort time into Array
        Array_merge.append(merge_time)
        # Appending Quicksort sort time into Array
        Array_quicksort.append(quicksort_time)
    plt.title('Sort Performance for Non-decreasing inputs')
    plot(sizes,Array_insertion,Array_merge,Array_quicksort)
# Plot for non-decreasing Input Values
def input_plot3():
    Array_insertion = []
    Array_merge = []
    Array_quicksort = []
    Arr1, Arr2, Arr3 = [], [], []
    # sizes = [5000, 10000, 15000, 20000, 25000, 30000]
    sizes = [500, 1000, 1500, 2000, 2500, 3000]
    # Iterating through the loop for given Sizes
    for i in sizes:
        Arr1 = Random(i)
        Arr1.sort(reverse=True)
        Arr2 = copy.deepcopy(Arr1)
        Arr3 = copy.deepcopy(Arr1)
        # time.time function used for Computing start and end time
        t0 = time.time()
        insertionsort(Arr1)
        t1 = time.time()
        insertion_time = t1 - t0
        t2 = time.time()
        mergeSort(Arr2)
        t3 = time.time()
        merge_time = t3 - t2
        t4 = time.time()
        quickSort(Arr3, 0, len(Arr3) - 1)
        t5 = time.time()
        quicksort_time = t5 - t4
        # Appending Selection sort time into Array
        Array_insertion.append(insertion_time)
        # Appending Insertion sort time into Array
        Array_merge.append(merge_time)
        # Appending quicksort sort time into Array
        Array_quicksort.append(quicksort_time)

    plt.title('Sort Performance for Non-increasing inputs')
    plot(sizes,Array_insertion,Array_merge,Array_quicksort)

# Input for Noisy non-decreasing Data
def input_plot4():
    avg_insertion = []
    avg_merge = []
    avg_quicksort = []
    Arr1, Arr2, Arr3 = [], [], []
    sum_insertion = 0
    sum_selection = 0
    sum_quicksort = 0
        sizes = [5000, 10000, 15000, 20000, 25000, 30000]
    # sizes = [500, 1000, 1500, 2000, 2500, 3000]
    # Iterating through the loop for given Sizes
    for i in sizes:
        sum_insertion = 0
        sum_merge = 0
        sum_quicksort = 0
        for k in range(0, 3):
            Arr1 = Random(i)
            Arr1.sort()
            Arr2 = copy.deepcopy(Arr1)
            Arr3 = copy.deepcopy(Arr1)
            # Creating random integer values for 50 iterations
            for c in range(0, 50):
                x = random.randint(0, i - 1)
                y = random.randint(0, i - 1)
                # Swapping array values in random order
                Arr1[x], Arr1[y] = Arr1[y], Arr1[x]
            # time.time function used for Computing start and end time
            t0 = time.time()
            insertionsort(Arr1)
            t1 = time.time()
            insertion_time = t1 - t0
            sum_insertion = insertion_time + sum_insertion
            # time.time function used for Computing start and end time
            t2 = time.time()
            # mergeSort(Arr2)
            t3 = time.time()
            merge_time = t3 - t2
            sum_merge = merge_time + sum_merge
            t4 = time.time()
            # quickSort(Arr3, 0, len(Arr3) - 1)
            t5 = time.time()
            quicksort_time = t5 - t4
            sum_quicksort = quicksort_time + sum_quicksort
        sum_merge = sum_merge / 3
        sum_insertion = sum_insertion / 3
        sum_quicksort = sum_quicksort / 3
        avg_insertion.append(sum_insertion)
        avg_merge.append(sum_merge)
        avg_quicksort.append(sum_quicksort)
    plt.title('Sort Performance for Noisy Non-decreasing inputs', fontsize=70,
              ha='center')
    plot(sizes,avg_insertion,avg_merge,avg_quicksort)

# Input for Small random Values
def input5():
    Arr1, Arr2, Arr3 = [], [], []
    A1 = []
    sum_insertion = 0
    sum_merge = 0
    sum_quicksort = 0
    for i in range(0, 100000):
        Arr1 = Random(50)
        Arr2 = copy.deepcopy(Arr1)
        Arr3 = copy.deepcopy(Arr1)
        t0 = time.time()
        insertionsort(Arr1)
        t1 = time.time()
        insertion_time = t1 - t0
        t2 = time.time()
        mergeSort(Arr2)
        t3 = time.time()
        merge_time = t3 - t2
        t4 = time.time()
        quickSort(Arr3, 0, len(Arr3) - 1)
        t5 = time.time()
        quicksort_time = t5 - t4
        sum_insertion = insertion_time + sum_insertion
        sum_merge = merge_time + sum_merge
        sum_quicksort = quicksort_time + sum_quicksort
    print("The total time taken to execute the Insertion Sort Query is :",
          sum_insertion, " Seconds")
    print("The total time taken to execute the Merge Sort Query is :",
          sum_merge, " Seconds")
    print("The total time taken to execute the Quicksort Query is :",
          sum_quicksort, " Seconds")


# Insertion sort with two passes
def insertionsort(A):
    # For input size in range of 0 to size-1
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key
    return A

def mergeSort(A):
    if len(A) > 1:
        mid = len(A) // 2
        L = A[:mid]
        R = A[mid:]
        mergeSort(L)
        mergeSort(R)
        i = 0
        j = 0
        k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            A[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            A[k] = R[j]
            j += 1
            k += 1
    return A

def partition(A, low, high):
    i = low - 1
    pivot = A[high]
    for j in range(low, high):
        if A[j] <= pivot:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[high] = A[high], A[i + 1]
    return i + 1


def quickSort(A, low, high):
    if low < high:
        q = partition(A, low, high)
        quickSort(A, low, q - 1)
        quickSort(A, q + 1, high)
    return A

def main():
    # Choose the function you'd like the carry out
    print(
        "Choose the Operation Number:\n 1.Large random inputs \n 2.Non-decreasing inputs \n 3.Non-increasing inputs \n 4.Noisy non-decreasing inputs \n 5.Small random inputs\n")
    option = int(input())

    if option == 1:

        input_plot1()
    elif option == 2:
        input_plot2()
    elif option == 3:
        input_plot3()
    elif option == 4:
        input_plot4()
    elif option == 5:
        input5()
    else:
        print("Undefined Input Value")


if __name__ == '__main__':
    # Executing the main function
    main()