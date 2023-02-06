def fibonacci(index):
    if index == 0:
        return 0
    elif index == 1:
        return 1
    return fibonacci(index-2) + fibonacci(index-1)

index = int(input())
print(fibonacci(index))
