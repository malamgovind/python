from multiprocessing import Pool

def square(n):
    return n*n

with Pool() as pool:

    result = pool.map(
        square,
        [1,2,3,4,5]
    )

print(result)