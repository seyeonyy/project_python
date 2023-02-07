def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)

def binary_search(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if arr[mid] == target:
        return mid

    elif arr[mid] > target:
        return binary_search(arr, target, start, mid -1)

    else:
        return binary_search(arr, target, mid + 1, end)

n = int(input())
fibonacci2 = []
for i in range(n+1):
    fibonacci2.append(fibonacci(i))

print(fibonacci2)
arr = fibonacci2
m = len(arr)
target = int(input())
res = binary_search(arr, target, 0, m-1)
print('피보나치 수열은 {}번째에 있습니다.'.format(res + 1))

