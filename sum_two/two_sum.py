def two_sum(nums: list, targ: int) -> list:
    temp = []
    for i, value in enumerate(nums):
        difference = targ - value
        if difference in temp:
            return [i, temp.index(difference)]
        temp.append(value)


def list_create(s: str) -> list:
    return [int(i) for i in s.split()]


numbers = list_create(input())
target = int(input())
print(two_sum(numbers, target))
