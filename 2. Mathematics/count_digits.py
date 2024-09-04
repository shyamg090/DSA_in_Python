def count_digits(n):

    if n == 0:
        return n
    
    if n < 9:
        return n
    
    count = 0
    while(n != 0 ):
        n = n%10
        print(n)
        count = count + 1
    return count

    # print(n//10)

print(count_digits(123))