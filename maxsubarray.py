arr = list(map(int, input("Enter: ").split()))
B = int(input())
A=len(arr)

max_sum = 0
current_sum = 0
start = 0

for end in range(len(arr)):
    current_sum += arr[end]
    
    while current_sum > B:
        current_sum -= arr[start]
        start += 1

    max_sum = max(max_sum, current_sum)

print(max_sum)
