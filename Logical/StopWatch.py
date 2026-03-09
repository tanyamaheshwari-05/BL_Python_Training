import time

input("Press enter to  Start Stopwatch. ")
start_time = time.time()

input("Press enter to  Stop Stopwatch. ")
end_time= time.time()

elapsed= end_time - start_time
print(f"Elapsed Time: {elapsed:.2f} seconds")