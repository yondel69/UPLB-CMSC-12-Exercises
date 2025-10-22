def bitonic(s):
    n_len = len(s)
    for peak in range(n_len): #check non-decreasing from start to peak
        non_decreasing = True
        for i in range(peak):
            if s[i] > s[i+1]:
                non_decreasing = False
                break
        if not non_decreasing: #check non-increasing from peak to end
            continue
        non_increasing = True
        for i in range(peak, n_len-1):
            if s[i] < s[i+1]:
                non_increasing = False
                break
        if non_increasing:
            return True
    return False

def largest_bitonic_at_most(n):
    s = str(n)
    if bitonic(s):
        return n #small n (n < 10000) iterate downwards
    if n < 10000:
        candidate = n - 1
        while candidate >= 0:
            if bitonic(str(candidate)):
                return candidate
            candidate -= 1
    else: #placeholder returns 0 for large n to avoid inf loop
        return 0

#sample calls
#print(largest_bitonic_at_most()) #input sa parenthesis    
