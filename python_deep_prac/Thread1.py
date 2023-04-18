import threading
import os


def foo():
    # print('thread_id', threading.get_native_id())
    print('process_id', os.getpid())

if __name__=='__main__':
    print('process_id', os.getpid())
    thread1 = threading.Thread(target=foo).start()
    thread2 = threading.Thread(target=foo).start()
    thread3 = threading.Thread(target=foo).start()

    # 같은 프로세스에 구성요소라서 pid 값이 같다. 