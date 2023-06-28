"""
##########################################
### Theory ###
    1. Default sort function in Python (Timsort algorithm)
        A built-in function that sorts a list.

    2. BUBBLE Sort (video: https://www.youtube.com/watch?v=lyZQPjUT5B4&ab_channel=AlgoRythmics)
        Computational complexity: O(n^2)
        For each step (0, len(list)) move the maximum element to the right on position len(list) -step -1.

    3. INSERTION Sort (video: https://www.youtube.com/watch?v=ROalU379l3U&ab_channel=AlgoRythmics)
        Computational complexity: O(n^2)
        For each step (1, len(list)) move the list[step] element to his position in relation with the numbers from the
        left.

    4. MERGE Sort (https://www.youtube.com/watch?v=XaqR3G_NVoo&ab_channel=AlgoRythmics)
        Computational complexity: O(n * log n)
        2 sorted lists are sorted together into 1 list. Use recursion function.
        example: (https://www.tutorialspoint.com/data_structures_algorithms/merge_sort_algorithm.htm)

    5. SELECTION Sort(https://www.youtube.com/watch?v=Ns4TPTC8whw&ab_channel=AlgoRythmics)
        Computational complexity: O(n^2)
        For each step (0, len(list)) find the lowest number and put it at index = step

    6. QUICK Sort ()
        Computational complexity: O(n * log n)
        Use a first element as a PIVOT (in the left sdewe have only lower numbers and in the right side we have only
        higher numbers)
        Do this recursive.

    7. Which one is faster?
        https://www.toptal.com/developers/sorting-algorithms

    8. Other SORTing algorithms and Complexity:
        (https://www.geeksforgeeks.org/time-complexities-of-all-sorting-algorithms/)
        Complexity comparation: https://www.happycoders.eu/algorithms/big-o-notation-time-complexity/
##########################################
"""

import random
import os

def show_menu():

    ### clear screen ###
    os.system('cls')

    print("\n")
    print("MENU")
    print("\n")

    print("1. Python BUILT-IN Sort")
    print("2. BUBBLE Sort")
    print("3. INSERTION Sort")
    print("4. MERGE Sort")
    print("5. SELECTION Sort")
    print("6. QUICK Sort")
    print("0. EXIT Sort")
    print("\n\n")

    choice = input()
    return choice

def python_sort(my_list):

    print(f"\n\n----------------------------------------------")
    print(f"--- START PYTHON SORT ---\n")

    #####################
    ### add code here ###
    result = sorted(my_list)
    return result
    #####################

    print(f"\n--- STOP PYTHON SORT ---")
    print(f"\n\n----------------------------------------------")


def bubble_sort(my_list):

    print(f"\n\n----------------------------------------------")
    print(f"--- START PYTHON SORT ---\n")

    #####################
    ### add code here ###
    sorted_list = [item for item in my_list]

    for i in range(len(sorted_list)):
        swap_was_not_made = True

        for j in range(len(sorted_list) - 1 - i):

            if sorted_list[j] > sorted_list[j + 1]:
                swap_was_not_made = False
                a = sorted_list[j]
                sorted_list[j] = sorted_list[j + 1]
                sorted_list[j + 1] = a

        if swap_was_not_made:
            break

    #####################

    print(f"\n--- STOP BUBBLE SORT ---")
    print(f"\n\n----------------------------------------------")

    return sorted_list
def insertion_sort(my_list):

    print(f"\n\n----------------------------------------------")
    print(f"--- START INSERTION SORT ---\n")

    #####################
    ### add code here ###
    sorted_list = [item for item in my_list]

    for i in range(1, len(sorted_list)):
        for k in range(i, 0, -1):

            if sorted_list[k] > sorted_list[k - 1]:
                break

            a = sorted_list[k]
            sorted_list[k] = sorted_list[k - 1]
            sorted_list[k - 1] = a
    #####################

    print(f"\n--- STOP INSERTION SORT ---")
    print(f"\n\n----------------------------------------------")

    return sorted_list


def merge_recursive(a_list):
    if len(a_list) == 1:
        return a_list

    mid = int(len(a_list) / 2)

    st = merge_recursive(a_list[:mid])
    dr = merge_recursive(a_list[mid:])

    c = []
    i = 0
    j = 0

    while i <= len(st) - 1 and j <= len(dr) - 1:
        if st[i] < dr[j]:
            c.append(st[i])
            i += 1

        else:
            c.append(dr[j])
            j += 1

    while i <= len(st) - 1:
        c.append(st[i])
        i += 1

    while j <= len(dr) - 1:
        c.append(dr[j])
        j += 1

    return c


def merge_sort(my_list):
    print(f"\n\n----------------------------------------------")
    print(f"--- START MERGE SORT ---\n")

    #####################
    ### add code here ###
    sorted_list = merge_recursive(my_list)
    #####################

    print(f"\n--- STOP MERGE SORT ---")
    print(f"----------------------------------------------\n\n")

    return sorted_list

def selection_sort(my_list):
    print(f"\n\n----------------------------------------------")
    print(f"--- START SELECTION SORT ---\n")

    #####################
    ### add code here ###

    #####################

    print(f"\n--- STOP SELECTION SORT ---")
    print(f"\n\n----------------------------------------------")

def quick_sort_recursive(my_list):

    ########################################################
    ### get pivot ###

    ########################################################
    ### combine left + pivot + right ###

    return None
    ########################################################

def quick_sort(my_list):
    print(f"\n\n----------------------------------------------")
    print(f"--- START QUICK-SORT ---\n")

    #####################
    ### add code here ###
    sorted_list = quick_sort_recursive(my_list)
    #####################

    print(f"\n--- STOP QUICK-SORT ---")
    print(f"\n\n----------------------------------------------")


def main():

    while True:

        random_list = random.sample(range(100), 10)
        sorted_list = None

        choice = show_menu()

        if choice == "0":
            break

        elif choice == "1":
            sorted_list = python_sort(random_list)

        elif choice == "2":
            sorted_list = bubble_sort(random_list)

        elif choice == "3":
            sorted_list = insertion_sort(random_list)

        elif choice == "4":
            sorted_list = merge_sort(random_list)

        print(f"random list: {random_list}")
        print(f"sorted list: {sorted_list}")

        print("\n\nPress ENTER to continue!")
        input()

if __name__ == '__main__':
    main()