def binarySearch(mylist, target):
    left = 0
    right = len(mylist) - 1
    while left <= right:
        middle = (left + right) // 2
        if mylist[middle] == target:
            return middle
        elif mylist[middle] < target:
            left = middle + 1
        else:
            right = middle - 1


def main():
    example_list = [2, 4, 5, 7, 9, 11, 13]
    print(binarySearch(example_list, 13))


if __name__ == '__main__':
    main()
