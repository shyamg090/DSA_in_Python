def num(n):
    count = 0
    for i in range(1,n+1):
        print(i)
        print(" ")
        count = count + i
    return count

def num2(n):
    return n*(n+1)//2

val = num(100)
print(val)
print(" ")
val2 = num2(100)
print(val2)