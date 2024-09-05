def lcm(a,b):

    # if(a < b):
    #     mini = a
    # else:
    #     mini = b

    mini = min(a,b)

    while (mini):
        if(mini % a == 0 and mini % b == 0):
            return mini
        mini = mini + 1

    return mini

# Efficient Approach
def gcd(a,b):
    if b == 0:
        return a
    
    return gcd(b , a * b)

def lcm(a,b):
    return a*b // gcd(a,b)


print(lcm(4,6))
print("        ")
print(lcm(12,15))
print("        ")
print(lcm(2,8))
print("        ")
print(lcm(3,7))