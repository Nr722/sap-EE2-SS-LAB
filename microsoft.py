def solution(array):
    additions = 0
    arr = array
    # Check if the sum of neighboring values is greater than or equal to 0
    for i in range(len(arr)):
        if i == 0:
            # For the first element, consider only i+1
            if arr[i] + arr[i + 1] < 0:
                addition = abs(arr[i] + arr[i + 1])
                arr[i+1] += addition
                additions += addition
        elif i == len(arr) - 1:
            # For the last element, consider only i-1
            if arr[i - 1] + arr[i] < 0:
                addition = abs(arr[i - 1] + arr[i])
                arr[i] += addition
                additions += addition
        else:
            # For all other elements, consider both i-1 and i+1
            if arr[i-1] + arr[i] + arr[i+1] < 0:
                addition = abs(arr[i-1] + arr[i] + arr[i+1] )
                arr[i+1] += addition
                additions += addition

    return additions

# Example usage:
arr = [1,1,1,1,-3]
result = solution(arr)
print("Updated Array:", arr)
print("Total Additions:", result)

