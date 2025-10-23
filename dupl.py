def remove_duplicates(arr):
    seen = set()
    result = []
    for num in arr:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result


numbers = [1, 2, 2, 3, 4, 4, 5, 1, 6]
result = remove_duplicates(numbers)
print(result)  