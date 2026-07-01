from multiprocessing import Pool

numbers=[1,2,3,4,5]

def cube(n):
    return n**3

with Pool() as pool:

    result=pool.map(cube,numbers)

print(result)