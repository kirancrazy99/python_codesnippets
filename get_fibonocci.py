def fibanocci_generator():
    a,b = 0,1
    while True:
        yield a
        a,b = b,a+b

for i in fibanocci_generator():
    if i>200:
        break
    print(i)