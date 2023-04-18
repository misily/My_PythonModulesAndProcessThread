# print('hello, os')

import os

# print('hello, os')
# print('my pid is', os.getpid())


from multiprocessing import Process

def foo():
    print('child process', os.getpid())
    print('my parent is', os.getpid())

if __name__ == '__main__':
    print('child process', os.getpid())
    child = Process(target=foo).start()
    child = Process(target=foo).start()
    child = Process(target=foo).start()


