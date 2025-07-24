# def my_decorator(func):
#   def wrapper():
#     print('***********************')
#     func()
#     print('***********************')
#   return wrapper

# def hello ():
#     print("hello")
#
# a=my_decorator(hello)
# a()

# @my_decorator
# def hello ():
#     print("hello")
#
# hello()

# import time
#
# def timer(func):
#   def wrapper(*args):
#     start = time.time()
#     func(*args)
#     print('time taken by',func.__name__,time.time()-start,'secs')
#   return wrapper
#
# @timer
# def hello():
#   print('hello wolrd')

# @timer
# def power(a,b):
#   print(a**b)
#
# # hello()
# power(1,1)

# def sanity_check(data_type):
#   def outer(func):
#     def inner(*args):
#       if data_type==type(*args):
#         func(*args)
#       else:
#         raise TypeError('this data type is not valid')
#     return inner
#   return outer
#
# @sanity_check(str)
# def sq(num):
#   print(num**2)
#
#
# @sanity_check(str)
# def greet(name):
#   print('hello',name)
#
# greet(1)