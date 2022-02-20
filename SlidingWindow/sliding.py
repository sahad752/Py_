

def brute(string, window):

    for i in range(len(string)-window+1):
        for j in range(window):
            print(string[i+j], end="")
        print("\n")

def bruteArray(array, window):
    cur_sum = 0
    max_sum = 0
    for i in range(len(array)-window+1):
        for j in range(window):
            cur_sum += array[i+j]
        max_sum = max(max_sum, cur_sum)
    
    print(max_sum)

def slidingArray(array, window):
    cur_sum = 0
    max_sum = 0
    for i in range(window):
        cur_sum += array[i]
    
    max_sum = cur_sum
    for i in range(window, len(array)):
        cur_sum += array[i] - array[i-window]
        max_sum = max(max_sum, cur_sum)
    
    print(max_sum)

brute('abcdefg', 3)

bruteArray([1,2,3,4,5,6,7,8,9,10], 3)