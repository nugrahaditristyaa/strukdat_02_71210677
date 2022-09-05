import timeit

# iteratif
def fibonacci_iteratif(n):
    lst = [0, 1, 1]
    for a in range(2, n):
        lst.append(lst[-1] + lst[-2])
    return lst[n]
for i in range(1, 101):
    starttime =timeit.default_timer()
    hsl = fibonacci_iteratif(i)
    endtime = timeit.default_timer()
    print("n =",i,",", hsl,"interatif: ",endtime-starttime)

# rekursif
def fibonacci_rekursif(n):
    if n < 2:
        return n
    return fibonacci_rekursif(n-2) + fibonacci_rekursif(n-1)
for i in range(1, 101):
    starttime = timeit.default_timer()
    hsl = fibonacci_rekursif(i)
    endtime = timeit.default_timer()
    print("n =",i,",", hsl,"rekursif: ",endtime-starttime)


    
