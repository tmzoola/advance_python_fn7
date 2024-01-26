import time
import threading
import concurrent.futures


start = time.perf_counter()

def do_smth(a):
    print(f"Reading a file .....{a}")
    time.sleep(a)
    print(f"Completed reading .....{a}")



with concurrent.futures.ThreadPoolExecutor() as executor:
    list_a = [5,4,3,2,1]
    res = executor.map(do_smth, list_a)


# thread = []

# for i in range(30):
#     t = threading.Thread(target=do_smth)
#     t.start()
#     thread.append(t)

# for t in thread:
#     t.join()

# t1 = threading.Thread(target=do_smth)
# t2 = threading.Thread(target=do_smth)
# t3 = threading.Thread(target=do_smth)

# t1.start()
# t2.start()
# t3.start()

# t1.join()
# t2.join()
# t3.join()



finish = time.perf_counter()

print(f"Funksiya ishlash tezligi {round(finish-start,2)}")