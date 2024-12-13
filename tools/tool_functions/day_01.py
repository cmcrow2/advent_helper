def location_ids(*args, **kwargs):
    '''Given the puzzle input, returns the total distance between lists.'''
    left_nums, right_nums = read_and_seperate_nums()

    result = 0
    # iterate over left_nums
    for i, num in enumerate(left_nums):
        # take the absolute value of the two nums and add to result
        result += abs(num - right_nums[i])

    return result


def similarity_score(*args, **kwargs):
    '''Given the puzzle input, returns the similarity score between lists.'''
    left_nums, right_nums = read_and_seperate_nums(False)
    result = 0
    # iterate over left_nums
    for num in left_nums:
        # check the count of current number in right_nums
        count = right_nums.count(num)
        # multiply the current number by result of count
        # add to result
        result += (num * count)

    return result


def read_and_seperate_nums(sort=True):
    '''Pulls the puzzle input and transforms it to something easily mutable.'''
    f = open('tools/tool_function_inputs/day_01.txt', 'r')
    lines = f.read().split('\n')
    f.close()
    left_nums = []
    right_nums = []
    for line in lines:
        split = line.split('   ')
        left_nums.append(int(split[0]))
        right_nums.append(int(split[1]))

    if sort:
        left_nums.sort()
        right_nums.sort()

    return left_nums, right_nums
