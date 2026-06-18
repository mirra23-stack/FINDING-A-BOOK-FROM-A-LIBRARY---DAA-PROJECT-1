def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return arr[index]  
    return "Book not found"   

dataset = ["0.01 - A world at arms", "0.02 - Band of Brothers", "0.03 - Mein Kampf", "0.04 - Unbroken", "0.05 - Golden Moments In Drizzles"]
target = "0.03 - Mein Kampf"

result = linear_search(dataset, target)
print(result)