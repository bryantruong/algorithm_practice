def shifted_arr_search(shiftArr, num):
    return recursive_binary_search(shiftArr, num, 0, len(shiftArr) - 1)


def recursive_binary_search(shifted_arr, target, start_i, stop_i):
    # Base Case
    if stop_i == start_i:
        if shifted_arr[start_i] == target:
            return start_i
        else:
            return -1
    midpoint = (start_i + stop_i) // 2
    if shifted_arr[midpoint] == target:
        return midpoint
    else:
        # [10, 11, 3, 4, 5]
        # Need to figure out which side to look at
        # The left side is scrambled
        result = None
        if shifted_arr[start_i] > shifted_arr[midpoint]:
            if target >= shifted_arr[start_i]:
                # Look at left side
                result = recursive_binary_search(shifted_arr, target, start_i, midpoint - 1)
            else:
                # Look at the right side
                result = recursive_binary_search(shifted_arr, target, midpoint + 1, stop_i)
        # The right side is scrambled
        if shifted_arr[stop_i] < shifted_arr[midpoint]:
            if target <= shifted_arr[stop_i]:
                # Look at right side
                result = recursive_binary_search(shifted_arr, target, midpoint + 1, stop_i)
            else:
                # Look at left side
                result = recursive_binary_search(shifted_arr, target, start_i, midpoint - 1)
        # We are in a normal portion of the array
        else:
            if target < shifted_arr[midpoint]:
                result = recursive_binary_search(shifted_arr, target, start_i, midpoint - 1)
            else:
                result = recursive_binary_search(shifted_arr, target, midpoint + 1, stop_i)
        return result



if __name__ == '__main__':
    print(shifted_arr_search([1, 2, 3, 4, 5, 0], 0))
"""
1, 2, 3, 4, 5

2, 3, 4, 5, 1 # First rotation

3, 4, 5, 1, 2 # Second rotation

Find the index of num in shiftArray
If num is not in shiftArray, return -1

Example: [9, 12, 17, 2, 4, 5]
# [2, 4, 5, 9, 12, 17]
num = 2

Should return 3

Binary search

Base case is when midpoint == num or when len(shiftArr) == 1 and does not equal num
Say we choose 17 as midpoint. 17 > 9, but 17 > 5. We also should compare to our goal num. 9 is greater than num, 5 is greater than num. Since midpoint (17) > stop, we know we want to look at the right side.

New shiftArr = [2,4,5]
midpoint is 4.

4 > num, so first look at left side. 4 > 2, and 4 < 5. We are in a normal part of the array. 
Since 2 is less than midpoint, take left side.

New shiftArr = [2]
midpoint = 2, so midpoint == 2. Done! 
Return True

Pass in start and stop indices, so that way we maintain the indices. And choose midpoint from start and stop indices
"""