import threading
import time
lock = threading.Lock()  #  Create a lock object

# def print_numbers():
#     for i  in range(5):
#         with lock:
#             print(f"Number {i}")
#         time.sleep(1)
#
# def print_letters():
#     s="ABCDE"
#     for i in s:
#         with lock:
#             print(f"Letter {i}")
#         time.sleep(1)
#
# t1=threading.Thread(target=print_numbers)
# t2=threading.Thread(target=print_letters)
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()

#
# c=0
# def c1():
#     global c
#     for i in range(100000):
#         # with lock:
#             c+=1
#
# def c2():
#     global c
#     for i in range(100000):
#         # with lock:
#         c+=1
#
# t1=threading.Thread(target=c1)
# t2=threading.Thread(target=c2)
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()
