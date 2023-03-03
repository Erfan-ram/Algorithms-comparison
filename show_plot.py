import time

start = time.time_ns() // 1e9

time.sleep(3)

end = time.time_ns() // 1e9

print(end-start)
