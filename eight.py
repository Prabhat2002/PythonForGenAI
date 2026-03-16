nums = list(map(int, input("Enter numbers: ").split()))
search = int(input("Enter number to search: "))
b = len(nums)
a = 0
while(a < b-1):
    mid = int( (a + b) / 2)
    if nums[mid] == search:
        print("Element found at index", mid)
        break
    elif nums[mid] < search:
        a = mid + 1
    else:
        b = mid - 1
else:
    print("Element not found")
