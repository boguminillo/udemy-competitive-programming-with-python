'''
Count Elements in array
Example 1:
Input arr = [10, 20, 20, 10, 10, 20, 5, 20]
Output: 10 3
        20 4
        5 1

Example 2:
Input arr = [10, 20, 20]
Output: 10 1
        20 2

solve it without using count function
'''

from collections import Counter


def countElements(arr):
    count_dict = {}
    for element in arr:
        if element in count_dict:
            count_dict[element] += 1
        else:
            count_dict[element] = 1
    return count_dict


def main():
    arr = [10, 20, 20, 10, 10, 20, 5, 20]
    counts = countElements(arr)
    for i in counts:
        print(str(i) + ' ' + str(counts[i]))
    # solution from collections module
    counts = Counter(arr)
    for i in counts:
        print(str(i) + ' ' + str(counts[i]))


if __name__ == '__main__':
    main()
