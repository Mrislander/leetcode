def printOutIteration(nums, left, right, mid, it):
    print()
    print()
    print("Iteration %s" % it)
    for idx, n in enumerate(nums):
        print(n, end=" ")

    print()
    for idx, var in enumerate(nums):
        if idx == left and idx != mid and idx != right:
            print('L', end=" ")
        elif idx == right and idx != mid and idx != left:
            print('R', end=" ")
        elif idx == mid and idx != left and idx != right:
            print('M', end=" ")
        elif idx == left and idx == mid and idx != right:
            print('L', end=" ")
            print()
            print(' '*2*idx + 'M', end=' ')
        elif idx == left and idx != mid and idx == right:
            print('L', end=" ")
            print()
            print(' ' * 2 * idx + 'R', end=' ')
        elif idx == mid and idx != left and idx == right:
            print('M', end=" ")
            print()
            print(' ' * 2 * idx + 'R', end=' ')
        elif idx == mid and idx == left and idx == right:
            print('L', end=" ")
            print()
            print(' ' * 2 * idx + 'R')
            print(' ' * 2 * idx + 'M', end=' ')
        else:
            print(' ', end=" ")


def binarySearch1(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1
    counter = 1
    while left <= right:
        mid = (left + right) // 2
        printOutIteration(nums, left, right, mid, counter)
        if nums[mid] == target:
            print()
            print("Found target in : %s" % mid)
            return mid
        elif nums[mid] < target:
            print()
            print("nums[mid](%s) < target(%s)" % (nums[mid], target))
            left = mid + 1
        else:
            print()
            print("nums[mid](%s) > target(%s)" % (nums[mid], target))
            right = mid - 1
        counter += 1
        print("next iteration left(%s) right(%s)" % (left, right))
    print()
    print("Hit the exit condition which is left(%s) > right(%s)" % (left, right))
    print("Didn't find the target")
    return -1

def binarySearch2(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return -1
    counter = 1
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        printOutIteration(nums, left, right, mid, counter)
        if nums[mid] == target:
            print()
            print("Found target in : %s" % mid)
            return mid
        elif nums[mid] < target:
            print()
            print("nums[mid](%s) < target(%s)" % (nums[mid], target))
            left = mid + 1
        else:
            print()
            print("nums[mid](%s) > target(%s)" % (nums[mid], target))
            right = mid
        counter += 1
        print("next iteration left(%s) right(%s)" % (left, right))
    print()
    print("Hit the exit condition which is left(%s) == right(%s)" % (left, right))
    print("Post-processing:")
    if left != len(nums) and nums[left] == target:
        print("found target(%s) in num[left] which is nums[%s]== target(%s)" % (target, left, target))
        return left
    print("Didn't find the target")
    return -1

def binarySearch3(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return -1
    counter = 1
    left, right = 0, len(nums) - 1
    window = 1
    while left + window < right:
        mid = (left + right) // 2
        printOutIteration(nums, left, right, mid, counter)
        if nums[mid] == target:
            print()
            print("Found target in : %s" % mid)
            return mid
        elif nums[mid] < target:
            print()
            print("nums[mid](%s) < target(%s)" % (nums[mid], target))
            left = mid
        else:
            print()
            print("nums[mid](%s) > target(%s)" % (nums[mid], target))
            right = mid
        counter += 1
        print("next iteration left(%s) right(%s)" % (left, right))
    print()
    print("Hit the exit condition which is left(%s) + width(%s) >= right(%s)" % (left, window, right))
    print("Post-processing:")
    if nums[left] == target:
        print("found target(%s) in  num[left] which is nums[%s]== target(%s)" % (target, left, target))
        return left
    if nums[right] == target:
        print("found target(%s) in  num[right] which is nums[%s] == target(%s)" % (target, right, target))
        return right
    print("Didn't find the target")
    return -1

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]
target = 0

print('***************Template 1****************')
print("Look for target number %s" % target)
ans = binarySearch1(nums, target)

print()
print('***************Template 2****************')
print("Look for target number %s" % target)
ans = binarySearch2(nums, target)

print()
print('***************Template 3****************')
print("Look for target number %s" % target)
ans = binarySearch3(nums, target)
