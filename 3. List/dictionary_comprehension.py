l1 = [10,10,20,20,10,20]

d2 = { x : x**3 for x in l1 if x % 2 == 0 }
d3 = { x : x**3 for x in l1 }

print(d2)
print('%%%%%%%%%%')
print(d3)

# op : {10: 1000, 20: 8000}

# op : {10: 1000, 20: 8000}