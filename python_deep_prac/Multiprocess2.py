from multiprocessing import Process
import os


def foo():
    print('This is foo')
    

def bar():
    print('This is bar')
    

def baz():
    print('This is baz')

if __name__ == '__main__':
    child = Process(target=foo).start()
    child = Process(target=bar).start()
    child = Process(target=baz).start()
    


