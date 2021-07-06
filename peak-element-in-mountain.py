'''
Peak Index in a Mountain Array

Example 1:
Inout arr = [0,2,1,0]
Output: 1

Example 2:
Inout arr = [3,4,5,1]
Output: 2

Example 3:
Input arr = [24,69,100,99,79,78,67,36,26,19]
Output: 2

solve it without using max function
'''


def linearPikeIndex(mount_array):
    # len-1 is used to avoid out of bound on arr[i+1]
    for i in range(0, len(mount_array)-1):
        if mount_array[i] > mount_array[i+1]:
            return i
    # since the last element is not tested in the loop if we get here return the last index
    return len(mount_array)-1


def binaryPikeIndex(mount_array):
    left = 0
    right = len(mount_array) - 1
    while left < right:
        middle = (left + right) // 2
        if mount_array[middle] > mount_array[middle+1]:
            right = middle
        else:
            left = middle + 1
    return left


def main():
    arr = [24, 69, 100, 99, 79, 78, 67, 36, 26, 19]
    print(linearPikeIndex(arr))
    print(linearPikeIndex(sorted(arr)))
    print(linearPikeIndex(sorted(arr, reverse=True)))
    print(binaryPikeIndex(arr))
    print(binaryPikeIndex(sorted(arr)))
    print(binaryPikeIndex(sorted(arr, reverse=True)))


if __name__ == '__main__':
    main()
