# exponential backoff
# problem : implement ab exponential backoff starategy 
#           that doubles the wait time beetween retries, 
#           starting from 1 second, but stop after 5 retries.

import time


wait_time = 1 
max_retries = 5 

for retry in range(1, max_retries + 1):
    print(f"attempt {retry}: waiting for {wait_time} seconds before retrying...")
    time.sleep(wait_time)
    wait_time = wait_time * 2
    print("retrying now...")

attempt = 0
while attempt < max_retries:
    print(f"attempt {attempt + 1}: waiting for {wait_time} seconds before retrying...")
    time.sleep(wait_time)
    wait_time = wait_time * 2
    attempt = attempt +1 
    print("retrying now...")