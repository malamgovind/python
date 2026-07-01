from concurrent.futures import ThreadPoolExecutor

def square(n):
    return n*n

with ThreadPoolExecutor() as executor:

    result = executor.map(
        square,
        [1,2,3,4,5]
    )

    print(list(result))