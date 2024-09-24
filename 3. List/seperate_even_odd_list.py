def evenodd(l):

    even = []
    odd = []

    for i in l:
        if i & 1 == 1:
            odd.append(i)
        else:
            even.append(i)

    return even, odd
    
    # print(even)
    # print('----------')
    # print(odd)

# evenodd([10,41,30,15,80])
# print('########')
# evenodd([10,30,40])

# we get as a tuple : destructuing the tuple
even, odd = evenodd([10,41,30,15,80])
print(even)
print(odd)

print('##############')

# or

def spe(l):
    odd = [ x for x in l if x & 1 == 1]
    even = [ x for x in l if x & 1 == 0]
    return even,odd

even, odd = spe([10,41,30,15,80])
print(even)
print(odd)