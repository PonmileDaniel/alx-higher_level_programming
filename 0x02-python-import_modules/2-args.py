#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    nums = len(sys.argv)
    if nums == 1:
        print('{} arguments.'.format(nums - 1))
    elif nums == 2:
        print('{} arguments:'.format(nums - 1))
    else:
        print('{} arguments:'.format(nums - 1))
    for n in range(1, nums):
        print('{}: {}'.format(n, sys.argv[n]))
