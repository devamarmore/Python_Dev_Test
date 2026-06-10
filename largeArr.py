def largest_consective(nums):
    num_set = set(nums)
    best = 0
    for n in num_set:
        if n-1 not in num_set:
            length = 1
        while n+ length in num_set:
            length += 1
            best = max(best,length)
        return best
    
    print(largest_consective([100,4,200,1,3,2]))
