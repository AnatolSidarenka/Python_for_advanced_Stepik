def virus(amount: int):
    name = 'anton'
    result = []
    for i in range(amount):
        count = 0
        string = input()
        for j in name:
            if j in string:
                count += 1
                string = string[string.find(j):]
        if count == 5:
            result.append(i + 1)
    return result


n = int(input())
print(*virus(n))