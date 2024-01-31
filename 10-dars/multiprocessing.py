import time
import multiprocessing


start = time.perf_counter()

def do_smthresh():
    print("do_smthresh....")
    time.sleep(1)
    print("do_smthresh finished")


if __name__ == '__main__':
    p1=multiprocessing.Process(target=do_smthresh)
    p2=multiprocessing.Process(target=do_smthresh)
    p1.start()
    p2.start()

    p1.join()
    p2.join()
    
finish = time.perf_counter()
print(f"finished in {round(finish-start)}")
