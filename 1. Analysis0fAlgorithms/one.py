# sum of n natural numbers

# Order of growth is constant
def fun(n):
    return n * (n+1) / 2

ans = fun(3)

print(" ")
print(ans)


# Order of growth is dependent on some operations happen in n times, whereas some happen in constant times
n = 3
sum = 0 #constant time

for i in range(0,n+1): 
    sum = sum + i     #n times
print(sum)    

# Order of growth is dependent on N square operation and an operation along with a constant Operation operation
def fun3(n):
    sum = 0 
    for i in range (1, n+1):
        for j in range (1, i+1):
            sum = sum + j
    return sum 

ans3 = fun3(3)

print(" ")
print (ans3)
