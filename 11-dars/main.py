import time
import os


def clock():
    start_time= round(time.time())
    while True:
        if (round(time.time())-start_time)%5==0:
            input()
            yield '5 secs'
            
        else:
            yield 0
        
def query():
    for i in os.walk('C:\\'):
        yield i[0]
    

def main():
    data = query()
    alarm = clock()

    while True:
        d= next(data)
        a = next(alarm)
        
        if a:
            print(a)
        else:
            print(d)
        time.sleep(1)

main()
# import asyncio
# import time

# start = time.perf_counter()

# async def func_one(secs):
#     await asyncio.sleep(secs)
#     print(f" Running .... {secs}")


# async def main():
#     async with asyncio.TaskGroup() as tg:
#         for i in range(6):
#             tg.create_task(func_one(i))
            

# asyncio.run(main())

# finish = time.perf_counter()
# print(f" Running in {round(finish-start,2)}")









# async def function_one():
#     print("I am Running .... 1")
    
# async def function_two():
#     await asyncio.sleep(5)
#     print("I am Running .... 2")
    
# async def function_three():
#     await asyncio.sleep(3)
#     print("I am Running .... 3")

# async def function_four():
#     print("I am Running .... 4")
    
# async def main():
#     task1 = asyncio.create_task(function_one())
#     task2 = asyncio.create_task(function_two())
#     task3 = asyncio.create_task(function_three())
#     task4 = asyncio.create_task(function_four())
    
#     await task1
#     await task2
#     await task3
#     await task4

# asyncio.run(main())





















# from tkinter import ttk
# import tkinter as tk
# import multiprocessing as mp
# import time


# def process():
#     time.sleep(10)


# def new_process():
#     p = mp.Process(target=process)
#     p.start()
#     lab['text'] = "After Run"

# if __name__ == "__main__":
#     root = tk.Tk()
#     root.geometry('500x500')
#     btn = ttk.Button(root, text="Run", command=new_process)
#     btn.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

#     lab = ttk.Label(root, text="Before Run")
#     lab.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

#     root.mainloop()