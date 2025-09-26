def can_divide( arr , k , limit):
    blocks = 1
    current_sum = 0
    for num in arr:
        if current_sum+num<=limit:
            current_sum+=num
        else:
            blocks+=1
            current_sum = num
            if blocks > k:
                return False
    return True

def minimize_largest_sum(arr , k):
    left = max(arr)
    right = sum(arr)
    answer = right
    while left <=right:
        mid = (left + right)//2
        if can_divide(arr , k , mid):
            answer = mid
            right = mid-1
        else:
            left = mid + 1
    return answer
n , k = map( int , input().split())
arr = list( map( int , input().split()))
print(minimize_largest_sum(arr , k))