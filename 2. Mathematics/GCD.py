def gcd(A,B):
    val = 1
    mini = 0

    if( A < B ):
        mini = A
    else:
        mini = B
    
    while(mini != 0 ):
        if(A % mini == 0) and (B % mini == 0):
            return mini
        else:
            mini = mini - 1
    return val


print(gcd (30,60))